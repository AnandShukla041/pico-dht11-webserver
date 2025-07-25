
# 🌡️ Real-Time Temperature and Humidity Monitoring Webserver

This project uses a **Raspberry Pi Pico W** and a **DHT11 temperature and humidity sensor** to create a real-time webserver that displays sensor data on your local Wi-Fi network.


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

> Sample Output:Temperature: 27°C
                 Humidity: 68%

Auto-refreshes every 5 seconds.

---

## 🧠 Project Author

**Anand Shukla**  
Intern @ Spectronic | Data Analyst Intern @ Coding Samurai  
GitHub: [@AnandShukla041](https://github.com/AnandShukla041)

---

## 📢 Share & Connect

If you like this project, feel free to ⭐️ it and connect on [LinkedIn](https://www.linkedin.com/in/anandshukla041).

"""

# Save the updated README.md
readme_path = "/mnt/data/README.md"
with open(readme_path, "w") as f:
    f.write(readme_content.strip())

readme_path

