import smtplib
import imghdr
from email.message import EmailMessage


PASSWORD = "demo"  # give your email id password
SENDER = "demoemail@gmail.com" # give your email id
RECEIVER = "demoemail@gmail.com"

def send_email(image_path):
    print("send email function start")
    email_message = EmailMessage
    email_message["Subject"] = " New Customer showed up!"
    email_message.set_conetent("hey, we just saw a new customer!")

    with open(image_path,"r") as file:
        content = file.read()
    email_message.add_attachment(content,maintype = "image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com",587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER,PASSWORD)
    gmail.sendmail(SENDER, RECEIVER,email_message)
    gmail.quit()
    print("send email function ended")

if __name__ == "__main__":
    send_email(image_path="images/19.png")