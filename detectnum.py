import cv2
import pytesseract
import os

# Set the path to the Tesseract executable (change to your Tesseract installation path)
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\Tesseract.exe'

# Define the path to the directory containing your images
image_dir = 'C:\\Users\\Ian\\132\\Freshmanexpo\\AutoDiceTower\\AutoDiceTower\\dicepics'

# Get a list of image file names in the directory
image_files = [f for f in os.listdir(image_dir) if f.endswith('.jpg')]

# Desired size for cropping
crop_size = 1000  # Set the crop size to 1000x1000

for image_file in image_files:
    # Construct the full path to the image
    image_path = os.path.join(image_dir, image_file)

    # Read the image using OpenCV
    image = cv2.imread(image_path)

    # Implement a dice detection method (you can use a pre-trained model for more accuracy)
    # Here's a simple example: 
    # Find contours to locate the dice based on edges, you can use more advanced methods for accuracy
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Assuming the largest contour is the dice, you can modify this logic accordingly
    largest_contour = max(contours, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(largest_contour)

    # Calculate the center of the dice
    center_x = x + w // 2
    center_y = y + h // 2

    # Calculate the cropping boundaries to keep the dice centered
    x1 = max(center_x - crop_size // 2, 0)
    y1 = max(center_y - crop_size // 2, 0)
    x2 = min(x1 + crop_size, image.shape[1])
    y2 = min(y1 + crop_size, image.shape[0])

    # Adjust the crop size to maintain a square aspect ratio
    crop_size = min(x2 - x1, y2 - y1)

    # Crop the image to focus on the dice
    dice_image = image[y1:y1 + crop_size, x1:x1 + crop_size]

    # Resize the cropped dice image to 1000x1000 pixels
    dice_image = cv2.resize(dice_image, (1000, 1000))

    # Display the resized dice image
    cv2.imshow('Dice Image', dice_image)
    cv2.waitKey(0)

    # Preprocessing
    gray_dice = cv2.cvtColor(dice_image, cv2.COLOR_BGR2GRAY)
    _, binary_dice = cv2.threshold(gray_dice, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Use pytesseract to extract text from the binary dice image
    extracted_text = pytesseract.image_to_string(binary_dice)

    # Extracted text might contain various characters; let's filter out digits
    extracted_numbers = ''.join(filter(str.isdigit, extracted_text))

    # Print the extracted numbers and the corresponding image file name
    print(f"Image: {image_file}, Extracted Numbers from Dice: {extracted_numbers}")

    # Close the image window
    cv2.destroyAllWindows()



