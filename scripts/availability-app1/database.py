from datetime import datetime
import sqlite3
from config import DB_NAME


def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        service TEXT,
        status TEXT,
        timestamp TEXT
    )''')
    conn.commit()
    conn.close()


def insert_log(service, status):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO logs (service, status, timestamp) VALUES (?, ?, ?)",
              (service, status, datetime.now()))
    conn.commit()
    conn.close()


def get_logs():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM logs")
    data = c.fetchall()
    conn.close()
    return data
