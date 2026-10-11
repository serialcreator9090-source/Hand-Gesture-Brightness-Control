# Hand Gesture Brightness Control

A computer vision project that uses hand tracking to control screen brightness through gestures. Built with Python, OpenCV, MediaPipe, NumPy, and Screen Brightness Control.

## Features

- Real-time hand tracking through a webcam
- Thumb and index fingertip distance measurement
- Maps finger distance to a brightness percentage between 0% and 100%
- Adjusts screen brightness dynamically
- Displays the current brightness percentage on the video feed
- Press `q` to exit

## Technologies Used

- Python
- OpenCV
- MediaPipe
- NumPy
- Screen Brightness Control

## How It Works

1. The webcam captures video frames.
2. MediaPipe detects hand landmarks.
3. The distance between the thumb tip and index fingertip is calculated.
4. The distance is mapped to a brightness percentage using NumPy interpolation.
5. The screen brightness is adjusted using the `screen_brightness_control` library.

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## How to Run

1. Connect a compatible display and allow webcam access.
2. Open a terminal in the project folder.
3. Run:

```bash
python BrightnessCtrlModule.py
```

4. Move your thumb and index finger closer together or farther apart to adjust brightness.
5. Press `q` to close the application.

## Requirements and Limitations

- A working webcam is required.
- Screen brightness adjustment depends on operating system, display hardware, and library support.
- The distance-to-brightness mapping may need calibration for different camera setups.
- The project has not been verified across all operating systems and displays.

## Author

Developed as a computer vision and gesture-control learning project.
