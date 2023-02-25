import smtplib


SENDER_EMAIL = "MyraGandhi20@gmail.com"
SENDER_PASSWORD = "ABCD"

def send_email(receiver_email, subject, body):
	message = "Subject is {} {{}".format(subject, body)
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
		server.login(SENDER_EMAIL,SENDER_PASSWORD)
		server.sendmail(SENDER_EMAIL, receiver_email, message)

