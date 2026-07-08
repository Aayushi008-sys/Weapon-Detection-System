import cv2
import numpy as np
import json
import os
from datetime import datetime

zone_points = []

def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(zone_points) < 4:
            zone_points.append((x, y))
            print(f"Point {len(zone_points)} added: {(x, y)}")

def draw_zone(frame, zone):
    pts = np.array(zone, np.int32)
    cv2.polylines(frame, [pts], True, (0, 0, 255), 2)

    cv2.putText(
        frame,
        "RESTRICTED AREA",
        (zone[0][0], zone[0][1] - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 0, 255),
        2
    )

def point_inside_polygon(point, polygon):
    return cv2.pointPolygonTest(
        np.array(polygon, np.int32),
        point,
        False
    ) >= 0

def draw_alert(frame, text):
    cv2.rectangle(frame, (0, 0), (frame.shape[1], 60), (0, 0, 255), -1)

    cv2.putText(
        frame,
        text,
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 255),
        2
    )

# ---------- SAVE / LOAD ZONE ----------
def save_zone(zone, path="zone.json"):
    with open(path, "w") as f:
        json.dump(zone, f)

def load_zone(path="zone.json"):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except:
        return None

# ---------- SAVE EVENT ----------
def save_event(frame, event_type):
    os.makedirs("output/snapshots", exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"output/snapshots/{event_type}_{timestamp}.jpg"

    cv2.imwrite(filename, frame)

    with open("output/logs.csv", "a") as f:
        f.write(f"{timestamp},{event_type},{filename}\n")