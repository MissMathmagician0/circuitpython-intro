import time
import serial
import smtplib

# the email address you want to send the email to
TO = {EMAIL_ADDRESS}

# the email account to use to send the mail from
# e.g. use gmail as they provide a free smtp server
GMAIL_USER = {YOUR_EMAIL}
GMAIL_PASS = {PASSWORD_OR_TOKEN}

SUBJECT = 'Sending mail via Bluefruit & Python script works!!'
TEXT = 'Your shake sensor detected shaking'

# you have to find out what exact address your usbmodem has on your computer
ser = serial.Serial('/dev/tty.usbmodem14201', 9600)

def send_email():
    print("Sending Email")
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(GMAIL_USER, GMAIL_PASS)
    header = 'To:' + TO + '\n' + 'From: ' + GMAIL_USER
    header = header + '\n' + 'Subject:' + SUBJECT + '\n'
    print(header)
    msg = header + '\n' + TEXT + ' \n\n'
    smtpserver.sendmail(GMAIL_USER, TO, msg)
    smtpserver.close()
    
while True:
    message = ser.readline()
    decoded_message = message.decode("utf-8")
    print(f"Message from Device: {decoded_message}")
    if "Device" in decoded_message:
        send_email()
    time.sleep(0.5)
