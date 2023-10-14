import cv2
import numpy as np

# ------------------------- Decoding YUV Data to Image -------------------------

# Read YUV bytes from the binary file
with open("received_yuv_data.bin", "rb") as yuv_file:
    yuv_bytes = yuv_file.read()

# Calculate the dimensions of the image
height = 480
width = 640

# Reshape YUV bytes to YUV image data
yuv_image = np.frombuffer(yuv_bytes, dtype=np.uint8).reshape((height, width, 3))

# Convert YUV image data to BGR color space
bgr_image = cv2.cvtColor(yuv_image, cv2.COLOR_YUV2BGR)

# Display the regenerated image
cv2.imshow("Regenerated Image", bgr_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the regenerated image to a file
cv2.imwrite("regenerated_image.png", bgr_image)
