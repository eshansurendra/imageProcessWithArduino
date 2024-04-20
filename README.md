# Image Processing with Arduino (VisionESP)

This repository contains a project focused on image processing using ESP32 microcontroller.

## Introduction
In this project, I've utilized Flask as the web framework and [pythonanywhere.com](https://www.pythonanywhere.com/) as the server to handle requests.

Initially, I set up the server side to handle POST requests, extracting text from them. Then, I stored this text in various formats such as CSV files and SQLite databases. The script `storeText.py` demonstrates this functionality.

Currently, the main focus of the project is on converting camera data into YUV format and transmitting it to the server. As a beginner in this domain, I took a gradual approach, building upon each step to eventually achieve the desired functionality. This is still a work in progress, with the implementation ongoing on Arduino.

The presence of multiple files in the repository reflects the iterative nature of the development process, with each file representing a step or experiment along the way.

## Files
- `binary_to_array.py`: Python script to convert binary data into arrays.
- `display.html`: HTML file for displaying images received from the server.
- `finalWorking.py`: Python script representing the final working code for image processing.
- `flaskWorkingFinal.py`: Flask app script for handling requests and storing data.
- `image.jpeg`, `image.jpg`, `image.png`, `image1.jpeg`: Sample image files.
- `postRequest.py`: Python script for making POST requests to the server.
- `received_yuv_data.bin`: Binary file containing YUV data received from the ESP32.
- `regenerated_image.png`: Regenerated image from the YUV data.
- `text.py`: Python script for text processing.
- `text_database.db`: SQLite database for storing text data.
- `yuvDecorder.py`: Python script for decoding YUV data.

## Usage
1. Set up your ESP32 microcontroller and connect it to the camera.
2. Ensure Flask is installed on your server (in this case, pythonanywhere.com).
3. Run the Flask app on the server to handle incoming requests.
4. Implement the Arduino code to capture camera data, convert it into YUV format, and send it to the server.

## References
- [Flask](https://flask.palletsprojects.com/): Python web framework used for server-side implementation.
- [ESP32](https://www.espressif.com/en/products/socs/esp32): Microcontroller used for image processing.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
