import smtplib
from config import ALERT_EMAIL


def send_alert(service):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(ALERT_EMAIL, "Singh#640")
        message = f"Subject: ALERT!\n\n{service} is DOWN!"
        server.sendmail(ALERT_EMAIL, ALERT_EMAIL, message)
        server.quit()
    except Exception as e:
        print("Alert failed:", e)
