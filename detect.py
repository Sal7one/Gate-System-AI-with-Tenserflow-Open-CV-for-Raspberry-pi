import sys
import cv2
from object_detector import ObjectDetector
from object_detector import ObjectDetectorOptions
import utils


def startHealthBarDetect(model: str, camera_id: int, width: int, height: int, num_threads: int,
        enable_edgetpu: bool) -> None:


  # Start capturing video input from the camera
  cap = cv2.VideoCapture(camera_id)
  cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
  cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)


  # Initialize the object detection model
  options = ObjectDetectorOptions(
      num_threads=num_threads,
      score_threshold=0.3,
      max_results=3,
      enable_edgetpu=enable_edgetpu)
  detector = ObjectDetector(model_path=model, options=options)
    
  
  # Continuously capture images from the camera and run inference
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      sys.exit(
          'ERROR: Unable to read from webcam. Please verify your webcam settings.'
      )

    image = cv2.flip(image, 1)

    # Run object detection estimation using the model.
    detections = detector.detect(image)

    # Draw keypoints and edges on input image
    image = utils.visualize(image, detections)
    
    # Get Probabilty
    probability = utils.getProbability(detections)


    barDetected = (probability *100) > 75
    # cv2.imshow('Tawakkalna bar', image)
    
    key = cv2.waitKey(3000) & 0xFF
    if (key == ord("q")):
        break
    
    if (barDetected):
        print("Tawakklena Bar Found")
        break


  cap.release()
  cv2.destroyAllWindows()