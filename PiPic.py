from picamera import PiCamera
import time
import keyboard
import shutil

# Define paths for USB storage and main storage
usb_storage_path = "/media/usb_drive/"
main_storage_path = "/home/pi/"

# Create a PiCamera object
camera = PiCamera()

try:
    while True:
        # Wait for the 'q' key press
        keyboard.wait('q')

        # Take a photo
        timestamp = time.strftime("%Y%m%d%H%M%S")
        photo_path = f"{main_storage_path}photo_{timestamp}.jpg"
        camera.capture(photo_path)
        print(f"Photo taken and saved as {photo_path}")

        # Check if the USB drive is mounted
        if shutil.disk_usage(usb_storage_path).total > 0:
            usb_photo_path = f"{usb_storage_path}photo_{timestamp}.jpg"
            shutil.copy(photo_path, usb_photo_path)
            print(f"Photo copied to USB storage: {usb_photo_path}")

finally:
    camera.close()
