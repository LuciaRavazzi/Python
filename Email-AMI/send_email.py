import smtplib
import ssl
from email.message import EmailMessage
from http import server

subject = "Email from python"
body = "Test email from python!"
sender_email = "#####@gmail.com"
password = input("Input a password: ")
receiver_email = "####@gmail.com"


# Google security -> enable less secure account (it works only for
# # gmail accounts which don't require 2-step verification).
message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.set_content(body)

html = f"""
<html>
    <body>
        <h1> {subject} </h1>
        <p> {body} </p>
    </body>
</html>
"""

message.add_alternative(html, subtype="html")

# secture connection.
context = ssl.create_default_context()

print("Sending email...")
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendemail(sender_email, receiver_email, message.as_string())

print("Success.")
