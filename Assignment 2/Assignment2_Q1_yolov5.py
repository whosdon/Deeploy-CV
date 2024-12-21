import cv2
import torch

# Load the YOLOv5 model (using 'yolov5s' for faster detection)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# Path to your video file
video_path = "sample_video.mp4"

# Initialize the video capture
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Cannot open video.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Cannot read frame.")
        break

    # Perform object detection with YOLOv5
    results = model(frame)

    # Render the results on the frame (draw bounding boxes and labels)
    results.render()  

    # Display the frame with detected objects
    cv2.imshow('YOLOv5 Real-Time Detection on Video', frame)

    # Exit if the user presses 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the resources
cap.release()
cv2.destroyAllWindows()
