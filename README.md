

## 📌 Overview

This project demonstrates how to integrate external APIs into a Python application, handle errors safely, and build a clean CLI-based user experience.

---

## ✨ Features

* 🌍 Fetch real-time weather by city
* 🌡️ Temperature in Celsius
* 💧 Humidity and weather conditions
* ⚠️ Graceful error handling (invalid API key, city not found)
* 🧪 Debug-friendly structure
* 🖥️ CLI + argument support

---

## 🧱 Tech Stack

* Python 3.8+
* `requests` library
* OpenWeatherMap API

---

## 📁 Project Structure

```bash id="9r9a4c"
weather-app/
├── weather.py
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup & Installation

### 1️⃣ Clone Repository

```bash id="19lq7d"
git clone https://github.com/your-username/weather-app.git
cd weather-app
```

### 2️⃣ Create Virtual Environment (recommended)

```bash id="cl34ak"
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash id="gflplr"
pip install -r requirements.txt
```

---

## 🔐 Environment Configuration

Create a `.env` file:

```env id="mbq66d"
API_KEY=your_api_key_here
```

Then update your code:

```python id="1lgd7j"
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")
```

---

## ▶️ Usage

### 🔹 Run with input prompt

```bash id="hr3h2y"
python weather.py
```

### 🔹 Run with command-line argument

```bash id="9pqb5n"
python weather.py Delhi
```

---

## 📊 Sample Output

```bash id="tds4ji"
City: Delhi
Temperature: 32°C
Weather: clear sky
Humidity: 40%
Wind Speed: 3.6 m/s
```
<img width="1581" height="607" alt="ECEAACB3-9488-4B25-943A-4615696B605B" src="https://github.com/user-attachments/assets/7fbc3ea7-3a9e-4a37-aa6b-a7f573d2bcad" />

---

## 🧠 Error Handling Strategy

| Scenario        | Handling                       |
| --------------- | ------------------------------ |
| Invalid API key | Displays API error message     |
| City not found  | Graceful fallback              |
| Missing fields  | Uses `.get()` to prevent crash |
| Network issues  | Try/except handling            |

---

## 🧪 Example Code Snippet

```python id="m0x24d"
try:
    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        print("Error:", data.get("message"))
    else:
        print("Temperature:", data["main"]["temp"])
except Exception as e:
    print("Something went wrong:", e)
```

---

## 🚀 Future Enhancements

* 📅 5-day / hourly forecast
* 📍 Auto-detect location (IP-based)
* 🖼️ GUI (Tkinter / PyQt)
* 🌐 Web version (Flask / FastAPI)
* 📦 Package as pip module

---

## 🧪 Testing Ideas

* Test invalid city names
* Simulate API failure
* Check empty input handling

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a new branch
3. Commit your changes
4. Open a pull request

---

## 📜 License

This project is licensed under the MIT License.

---

## 🙏 Acknowledgements

* OpenWeatherMap API for providing weather data
* Python community

---
