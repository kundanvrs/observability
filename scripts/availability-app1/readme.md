
## 🚀 Features

- 🔍 Monitor multiple services (HTTP endpoints)
- 🗄️ Store logs in SQLite database
- 📊 Calculate uptime percentage
- 🌐 REST API for logs and uptime
- 📧 Email alerts on failures
- ⚙️ Config-driven design

---

## 📁 Project Structure

```

uptime-monitor/
├── app.py           # Flask API (dashboard)
├── monitor.py       # Service health checker
├── database.py      # DB operations
├── alert.py         # Alerting (email)
├── config.py        # Configuration
└── requirements.txt # Dependencies

````


### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

### 🔹 Start monitoring (Terminal 1)

```bash
python monitor.py
```

---

### 🔹 Start API server (Terminal 2)

```bash
python app.py
```

---

## 🌐 Access the Application

| Endpoint  | Description       |
| --------- | ----------------- |
| `/`       | Health check      |
| `/logs`   | View all logs     |
| `/uptime` | Uptime percentage |

Open in browser:

```
http://localhost:5000/uptime
http://localhost:5000/logs
```

---

## 🧠 How It Works

1. `monitor.py` continuously checks configured URLs
2. Status (`UP`/`DOWN`) is stored in SQLite
3. `app.py` exposes APIs to fetch logs and uptime
4. Alerts are triggered on failures

---

## ⚡ Configuration

Edit `config.py`:

```python
URLS = [
    "https://example.com/health",
    "https://api.example.com/health"
]

CHECK_INTERVAL = 60  # seconds
DB_NAME = "uptime.db"
```

---

## 📊 Example Uptime Calculation

```
Uptime (%) = (Successful Checks / Total Checks) * 100
```

---

## 🔔 Alerts

* Email alerts are sent when a service is DOWN
* Configure credentials in `alert.py`

---
