import cv2
import numpy as np
import pytesseract
import tkinter as tk
from tkinter import messagebox
from picamera import PiCamera
from picamera.array import PiRGBArray

# Initialize the Pi Camera
camera = PiCamera()
camera.resolution = (640, 480)
raw_capture = PiRGBArray(camera, size=(640, 480))

# Create a tkinter window
root = tk.Tk()
root.title("Dice Number Detector")

# Create a label to display the camera feed
label = tk.Label(root)
label.pack()

# Function to update the camera feed
def update_camera_feed():
    # Capture an image
    camera.capture(raw_capture, format="bgr")
    image = raw_capture.array

    # Perform image processing to isolate the die
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresholded = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:
        # Assuming you have identified the contour that represents the die, crop the image
        x, y, w, h = cv2.boundingRect(contours[0])
        die_image = image[y:y+h, x:x+w]

        # Use OCR to recognize the number on the die
        number = pytesseract.image_to_string(die_image)

        if number:
            # Show the recognized number in a messagebox
            messagebox.showinfo("Die Number Detected", "Die shows: " + number)

    # Convert the OpenCV image to a format tkinter can display
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (640, 480))
    img = Image.fromarray(img)
    img = ImageTk.PhotoImage(image=img)

    label.img = img
    label.config(image=img)
    
    # Clear the camera buffer
    raw_capture.truncate(0)

    # Repeat this function after a delay (e.g., 100 milliseconds)
    root.after(100, update_camera_feed)

# Start the camera feed
update_camera_feed()

# Run the tkinter main loop
root.mainloop()

# Clean up
cv2.destroyAllWindows()
camera.close()
