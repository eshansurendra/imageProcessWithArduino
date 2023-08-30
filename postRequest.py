import cv2
import requests

# Load the image
image_path = "image1.jpeg"  # Replace with the actual image filename
image = cv2.imread(image_path)

# Resize the image to 640x480
image = cv2.resize(image, (640, 480))

# Convert the image to YUV color space
yuv_image = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)

# Convert YUV image to bytes
yuv_bytes = yuv_image.tobytes()


# Define the URL to send the POST request
url = "http://eshansurendraTest.pythonanywhere.com/decode_yuv"

# Send POST request with YUV data
response = requests.post(url, data=yuv_bytes)

# Print response from the server
print("Response from server:", response.text)
