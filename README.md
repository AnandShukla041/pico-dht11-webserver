
# 🌡️ Real-Time Temperature and Humidity Monitoring Webserver

This project uses a **Raspberry Pi Pico W** and a **DHT11 temperature and humidity sensor** to create a real-time webserver that displays sensor data on your local Wi-Fi network.

## 📷 Project Setup

### Circuit Diagram
![Circuit Diagram](images/circuit_diagram.png)

### Live Setup
![Live Hardware](images/live_setup.jpg)

---

## 🎬 Demo Video

📽️ [Click to Watch Demo](video/raspberry-pi-webserver.mp4)

---

## 🔧 Features

- 📡 Connects to Wi-Fi and serves a live webpage
- 🌡️ Displays real-time temperature and humidity
- 🔁 Auto-refresh every 5 seconds
- 💻 Works with MicroPython on Pico W

---

## 🧰 Hardware Used

- Raspberry Pi Pico W
- DHT11 Sensor (Temperature & Humidity)
- Jumper Wires
- Breadboard (optional)

---

## 🔌 Circuit Connection

| DHT11 Pin | Connects To Pico W |
|----------:|:-------------------|
| VCC       | 3.3V               |
| DATA      | GP15               |
| GND       | GND                |

---

## 🚀 Setup Instructions

1. Flash MicroPython firmware on your Pico W
2. Use Thonny or mpremote to upload `main.py`
3. Edit your Wi-Fi credentials in `main.py`
4. Open the serial monitor to find the IP address
5. Access the live data from a browser on the same Wi-Fi

---

## 🌐 Web Output Preview

> Sample Output:
