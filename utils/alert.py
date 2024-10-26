import smtplib
from email.mime.text import MIMEText
from config import ALERT_EMAIL, SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASSWORD

def send_alert(endpoint, results):
    msg_content = f"Alert! Issues detected on {endpoint}:\n\n" + "\n".join(
        [f"{check}: {result['details']}" for check, result in results.items() if not result['status']]
    )
    msg = MIMEText(msg_content)
    msg['Subject'] = f"ADC Alert for {endpoint}"
    msg['From'] = SMTP_USER
    msg['To'] = ALERT_EMAIL
    
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.sendmail(SMTP_USER, ALERT_EMAIL, msg.as_string())
    except Exception as e:
        print(f"Failed to send alert: {e}")
