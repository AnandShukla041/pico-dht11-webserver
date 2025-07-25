# Real-Time Temperature and Humidity Monitoring Webserver

This project uses a Raspberry Pi Pico W and a DHT11 sensor to create a simple webserver that displays real-time temperature and humidity data.

## Features

- WiFi connection to local network
- DHT11 sensor integration via GPIO
- Live web dashboard refreshes every 5 seconds
- Designed to run with MicroPython

## Hardware Used

- Raspberry Pi Pico W
- DHT11 Temperature and Humidity Sensor
- Jumper Wires

## Setup Instructions

1. Flash MicroPython onto the Pico W.
2. Connect the DHT11 to the correct GPIO (GPIO15 for data).
3. Replace WiFi credentials in `main.py`.
4. Upload the script to your Pico using Thonny or another tool.
5. Run the script and access the web interface on the Pico's IP address.