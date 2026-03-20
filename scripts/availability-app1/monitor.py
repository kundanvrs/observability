import requests
import time
from config import URLS, CHECK_INTERVAL
from database import insert_log
from alert import send_alert


def check_service(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return "UP"
    except:
        pass
    return "DOWN"


def run_monitor():
    while True:
        for url in URLS:
            status = check_service(url)
            insert_log(url, status)
            print(url, status)

            if status == "DOWN":
                send_alert(url)

        time.sleep(CHECK_INTERVAL)
run_monitor()