import cv2
import os

# Load the pre-trained MobileNet SSD model and its configuration
model_path = "ssd_mobilenet_v2_coco/frozen_inference_graph.pb"
config_path = "ssd_mobilenet_v2_coco.pbtxt"

# Load the model and its configuration
net = cv2.dnn.readNetFromTensorflow(model_path, config_path)

# Path to the folder containing the images
image_folder = 'C:\\Users\\Ian\\132\\Freshmanexpo\\AutoDiceTower\\AutoDiceTower\\dicepics'

# Get a list of all JPG files in the folder
jpg_files = [f for f in os.listdir(image_folder) if f.lower().endswith('.jpg')]

# Loop through each image file in the folder
for image_file in jpg_files:
    # Load the image
    image_path = os.path.join(image_folder, image_file)
    image = cv2.imread(image_path)

    # Prepare the image for object detection
    blob = cv2.dnn.blobFromImage(image, 0.007843, (300, 300), 127.5)

    # Set the image as input to the network
    net.setInput(blob)
    
    # Run forward pass to detect objects
    detections = net.forward()

    # Loop through the detected objects
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:  # Adjust the confidence threshold as needed
            # Get the coordinates of the object's bounding box
            box = detections[0, 0, i, 3:7] * [image.shape[1], image.shape[0], image.shape[1], image.shape[0]]
            (startX, startY, endX, endY) = box.astype(int)

            # Draw a rectangle around the object
            cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)

    # Display the image with the detected objects
    cv2.imshow('Object Detection', image)
    cv2.waitKey(0)

cv2.destroyAllWindows()
