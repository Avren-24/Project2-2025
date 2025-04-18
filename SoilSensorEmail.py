import RPi.GPIO as GPIO
import time
import smtplib
from email.message import EmailMessage
from datetime import datetime

# Soil Sensor Configuration
channel = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

# Email Configuration
from_email_addr = "1552038394@qq.com"
from_email_pass = "kayyffzchnoohade"
to_email_addr = "1552038394@qq.com"

# Function to check water status
def check_water_status(channel):
    if GPIO.input(channel):
        return "Water NOT needed"  # Dry soil
    else:
        return "Please water your plant"  # Wet soil

# Function to send an email
def send_email(status):
    msg = EmailMessage()
    body = f"Plant Status Report: {status}"
    msg.set_content(body)
    msg['From'] = from_email_addr
    msg['To'] = to_email_addr
    msg['Subject'] = 'Daily Plant Status Report'

    server = smtplib.SMTP('smtp.qq.com', 587)
    server.starttls()
    server.login(from_email_addr, from_email_pass)
    server.send_message(msg)
    print(f'Email sent: {status}')
    server.quit()

# Main loop to take readings at specific times
def main():
    daily_times = ["08:00", "12:00", "16:00", "20:00"]  # Daily reading times
    while True:
        now = datetime.now().strftime("%H:%M")  # Get current time in HH:MM format
        if now in daily_times:
            status = check_water_status(channel)
            print(f"{now}: {status}")
            send_email(status)
            time.sleep(60)  # Sleep for 1 minute to avoid multiple emails at the same time
        time.sleep(10)  # Check every 10 seconds

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
