import smtplib
from config import from_addr,to_addr,APP_PASS


def send_alert(service):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(ALERT_EMAIL, APP_PASS)
        message = f"Subject: ALERT!\n\n{service} is DOWN!"
        server.sendmail(from_addr, to_addr, message)
        server.quit()
    except Exception as e:
        print("Alert failed:", e)
