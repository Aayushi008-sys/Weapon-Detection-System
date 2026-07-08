import cv2
from detector import ObjectDetector
from utils import *

VIDEO_PATH = "http://192.168.179.32:8080/video"

detector = ObjectDetector()
cap = cv2.VideoCapture(VIDEO_PATH)
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

ret, first_frame = cap.read()
if not ret:
    print("Error loading video")
    exit()

# ================= LOAD / DRAW ZONE =================
restricted_zone = load_zone()

if restricted_zone is None:
    cv2.namedWindow("Draw Zone")
    cv2.setMouseCallback("Draw Zone", mouse_callback)

    while True:
        temp = first_frame.copy()

        for point in zone_points:
            cv2.circle(temp, point, 5, (0, 0, 255), -1)

        if len(zone_points) == 4:
            restricted_zone = zone_points.copy()
            save_zone(restricted_zone)
            break

        cv2.imshow("Draw Zone", temp)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            exit()

    cv2.destroyWindow("Draw Zone")

# ================= MAIN LOOP =================
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    knife_detected = False
    armed_intrusion = False
    normal_intrusion = False

    draw_zone(frame, restricted_zone)

    # ---------- KNIFE DETECTION ----------
    knife_results = detector.detect_knife(frame)

    for r in knife_results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

            knife_detected = True

            if point_inside_polygon((cx, cy), restricted_zone):
                armed_intrusion = True

    # ---------- PERSON DETECTION ----------
    person_results = detector.detect_person(frame)

    for r in person_results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

            if point_inside_polygon((cx, cy), restricted_zone):
                normal_intrusion = True

    # ---------- ALERT ----------
    if armed_intrusion:
        draw_alert(frame, "CRITICAL ALERT")
        save_event(frame, "armed_intruder")

    elif knife_detected:
        draw_alert(frame, "KNIFE DETECTED")
        save_event(frame, "knife")

    elif normal_intrusion:
        draw_alert(frame, "INTRUSION")
        save_event(frame, "intrusion")

    cv2.imshow("Surveillance", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()