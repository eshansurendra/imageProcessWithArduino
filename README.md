# Image Processing with Arduino

This repository contains a simple implementation to try image processing with ESP32 microcontroller.

## Introduction
In this project, I used [pythonanywhere.com](https://www.pythonanywhere.com/) as my server and utilized Flask as my web framework.

As the first step, I set up the server side to handle requests. Being a beginner in this area, I initially attempted to extract some text from the POST requests that came to the server. Then, I tried storing that text in a file on the server as a CSV file. Additionally, I experimented with storing the text in a SQLite database. My attempts were successful. I've included the file named `storeText.py` in this repository.

## Implementation
Currently, the project involves converting camera data into YUV format and sending it to the server. This part is still a work in progress as I'm trying to implement it on Arduino.

## Files
- `storeText.py`: Python script to handle POST requests, extract text, and store it in a file or SQLite database.
- Other files related to Arduino implementation (work in progress).

## Usage
1. Set up your ESP32 microcontroller and connect it to the camera.
2. Ensure Flask is installed on your server (in this case, pythonanywhere.com).
3. Run the Flask app on the server to handle incoming requests.
4. Implement the Arduino code to capture camera data, convert it into YUV format, and send it to the server.

## References
- [Flask](https://flask.palletsprojects.com/): Python web framework used for server-side implementation.
- [ESP32](https://www.espressif.com/en/products/socs/esp32): Microcontroller used for image processing.

