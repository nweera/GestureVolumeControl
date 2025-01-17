# Gesture Volume Control Project

## Description
This project implements a gesture-controlled volume adjustment system using hand tracking. By detecting the distance between your thumb and index finger, you can control your computer's volume level in real-time. The project uses computer vision through OpenCV and MediaPipe for hand tracking, combined with pycaw for Windows audio control.

## Features
- Real-time hand gesture detection
- Volume control through finger movements
- Visual feedback with:
  - Hand landmark tracking
  - Line visualization between thumb and index finger
  - Volume level indicator
  - FPS counter
- Smooth volume interpolation
- Windows system volume integration

## Prerequisites
To run this project, you need to install the following dependencies:
```bash
pip install opencv-python
pip install mediapipe
pip install numpy
pip install pycaw
pip install comtypes
```

## Project Structure
- `HandTrackingModule.py` - The hand tracking module providing hand detection functionality
- `VolumeControl.py` - Main script implementing the gesture-based volume control

## How It Works
1. The system detects hand landmarks using the MediaPipe library
2. It tracks the distance between the thumb (landmark 4) and index finger (landmark 8)
3. This distance is interpolated to map to your system's volume range
4. Volume is adjusted in real-time based on the finger distance:
   - Larger distance = Higher volume
   - Smaller distance = Lower volume
   - When fingers are very close (< 50 pixels), the center point turns green

## Usage
Run the volume control script:
```bash
python VolumeControl.py
```

### Gesture Guide
- Move your thumb and index finger apart to increase volume
- Bring them closer to decrease volume
- The pink line between your fingers shows the current distance
- A green dot appears when fingers are close enough to trigger minimum volume

## Configuration
The script includes several configurable parameters:
- Camera resolution: `wCam, hCam = 640, 480`
- Detection confidence: `detector = htm.handDetector(detectionCon=0.5)`
- Volume range mapping: Adjusts between system volume range (-65.25, 0.0)
- Gesture distance range: 15-200 pixels (can be adjusted based on your needs)

## System Requirements
- Windows operating system (pycaw is Windows-specific)
- Webcam
- Python 3.7 or higher

## Credits
This project was created following the tutorial by [Murtaza's Workshop - Robotics and AI](https://www.youtube.com/watch?v=9iEPzbG-xLE).

## License
This project is open source and available under the MIT License.

## Troubleshooting
- If the volume control is too sensitive, adjust the interpolation range in the code
- Ensure good lighting for optimal hand detection
- Keep your hand within the camera frame
- If volume control doesn't work, check if pycaw is properly installed and has necessary permissions
