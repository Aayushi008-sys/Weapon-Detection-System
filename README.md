# 🛡️ Real-Time Weapon Detection & Restricted Zone Intrusion Monitoring

An AI-powered smart surveillance system that detects knives and monitors restricted zones in real time using **YOLOv8**, **OpenCV**, and **Python**.
## 📌 Project Overview

This project is an AI-powered smart surveillance system designed to improve security by detecting weapons and monitoring restricted areas in real time. It combines computer vision and deep learning to identify persons and knives, detect intrusions, generate alerts, and automatically save snapshots with event logs.

The system uses a custom-trained YOLO model for knife detection and YOLOv8 for person detection, making it suitable for surveillance in restricted or high-security environments.
## 🚀 Features

- 🎥 Real-time surveillance using IP Webcam
- 👤 Person detection using YOLOv8
- 🔪 Knife detection using a custom YOLO model
- 🚧 User-defined restricted zone
- 🚨 Intrusion detection inside restricted areas
- ⚠️ Critical alert when a person carrying a knife enters the restricted zone
- 📸 Automatic snapshot capture of detected events
- 📝 Event logging with timestamps
- 💾 Automatic saving of restricted zone coordinates
## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| OpenCV | Image processing and video streaming |
| YOLOv8 | Person detection |
| Custom YOLO Model | Knife detection |
| NumPy | Numerical operations |
| IP Webcam | Live camera streaming from mobile device |
## 📂 Project Structure

```text
Weapon-Detection-System/
│
├── detector.py          # Weapon and person detection models
├── main.py              # Main application
├── utils.py             # Utility functions
├── weights/             # YOLO model weights
├── videos/              # Sample input videos
├── output/              # Saved snapshots and logs
├── requirements.txt     # Project dependencies
├── README.md            # Project documentation
└── .gitignore           # Ignored files
```
## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Aayushi008-sys/Weapon-Detection-System.git
```

### 2. Navigate to the project folder

```bash
cd Weapon-Detection-System
```

### 3. Install the required libraries

```bash
pip install -r requirements.txt
```
