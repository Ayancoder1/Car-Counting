# 🚗 Car Counter using YOLOv8 + OpenCV

A **real-time car counting system** built using **YOLOv8 object detection + tracking**, OpenCV, and Python.
This project detects cars from video footage and counts them automatically when they cross a defined line.

Perfect for:

* Smart traffic monitoring
* Computer vision learning projects
* AI + Embedded / IoT applications
* Portfolio / college project demos

---

## 🎥 Working Demo

👉 Add your demo video link here:

```
## 🎥 Demo Video
[Watch Working Video](PASTE_YOUR_VIDEO_LINK_HERE)
```
---

## ✨ Features

✔ Real-time car detection using **YOLOv8**
✔ Vehicle tracking with unique IDs
✔ Automatic line-crossing counter
✔ ROI masking support
✔ Simple and beginner-friendly code
✔ Works on recorded traffic videos

---

## 📂 Project Structure

```
Car-Counter/
│
├── car_counter.py          # Main Python code
├── mask.png                # Region of interest mask
├── Video_1.mp4             # Input traffic video
├── yolov8l.pt              # YOLO model weights
└── README.md
```

---

## ⚙️ Requirements

Install dependencies:

```bash
pip install ultralytics opencv-python cvzone numpy
```

---

## ▶️ How to Run

### 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/car-counter.git
cd car-counter
```

### 2️⃣ Add Required Files

Make sure you have:

* YOLO weight file (`yolov8l.pt`)
* Input video
* Mask image

Update paths in code if needed.

### 3️⃣ Run Script

```bash
python car_counter.py
```

Press **Q** to stop the video.

---

## 🧠 How It Works (Simple Explanation)

### 1. Object Detection

YOLOv8 detects vehicles from each video frame.

### 2. Tracking

Each detected car gets a **unique tracking ID**.

### 3. Region Masking

Mask limits detection to the road area only.

### 4. Line Crossing Logic

When a car center crosses the defined line:

```
(line_y - offset) < cy < (line_y + offset)
```

➡ That car gets counted once.

---

## 📊 Output Example

* Bounding box around each car
* Car ID label
* Center tracking dot
* Live total car count

---

## 🔧 Customization Ideas

You can easily:

* Count bikes, buses, trucks
* Add speed estimation
* Export data to CSV
* Use live CCTV feed
* Deploy on edge devices

---

## 🚀 Future Improvements

* Web dashboard
* Multi-lane detection
* Edge AI optimization
* Night traffic detection

---

## 👨‍💻 Author

**Ayan Kar**
AI • Embedded Systems • Computer Vision

If you like this project:

⭐ Star the repo
🍴 Fork it
🤝 Contribute
