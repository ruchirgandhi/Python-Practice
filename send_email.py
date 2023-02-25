import smtplib

port = 465
#password =  input("Please enter your password here:     ")

password = "ABCD"


SENDER_EMAIL = 'myragandhi20@gmail.com'
SENDER_PASSWORD = password

def send_email(receiver_email, subject, body):
    message = 'Subject: {}\n\n{}'.format(subject, body)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver_email, message)





