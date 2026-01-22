# Air Writing with Finger (Python)

This simple project lets you **draw or write in the air using your finger** tracked through your webcam. It uses **OpenCV** for image handling and **MediaPipe** for accurate hand and fingertip detection.

---

## 📋 Requirements

Make sure you have Python 3.7 or higher installed. Then install the following libraries:

```bash
pip install opencv-python mediapipe numpy
```

If your project includes multiple files (like `HandTrackingModule.py`), ensure they are in the same directory.

---

## ▶️ How to Run

1. Save all code files in the same folder.
2. Make sure the `Header` folder (with header images) exists if used.
3. Run the main file:

   ```bash
   python VirtualPaint.py
   ```
4. A webcam window will open.
5. Use your **index finger** to draw in the air.
6. Use **two fingers** to switch color modes.
7. Move your finger over the top bar area to change colors or activate eraser.
8. Press `Ctrl + C` or close the window to exit.

---

## 🧠 How It Works

* The webcam feed is captured frame by frame using `cv2.VideoCapture(0)`.
* MediaPipe detects **hand landmarks** in real time.
* The **index fingertip (id = 8)** is used as the drawing point.
* The motion of the fingertip is tracked, and a line is drawn between consecutive points.
* Using hand gestures (one finger for drawing, two for selection), users can write or erase on a virtual canvas.
* OpenCV overlays this drawing on top of the live camera feed.

---

## 🧩 File Structure

```
air-writing/
├── VirtualPaint.py         # Main drawing script
├── HandTrackingModule.py   # Custom module for hand tracking
├── Header/                 # Folder with header images
└── README.md               # (this file)
```

---

## ⚙️ Customization

You can modify:

* `brushThickness` → Thickness of the drawing line.
* `eraserThickness` → Thickness when erasing.
* `drawColor` → Default drawing color.
* Add or change header images to customize your tool bar.

---

## 🧾 Example

When you run the script:

* Point your **index finger** to draw.
* Raise **both index and middle fingers** to switch tools.
* Move to the top of the screen to select brush color or eraser.
* The FPS counter shows your webcam processing speed.

---

## 💡 Tips

* Ensure good lighting for accurate detection.
* Keep your hand inside the camera frame.
* Adjust camera resolution if the frame rate drops.

---

## 📜 License

Free to use for learning and demonstration purposes.
