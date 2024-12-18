#module that receives message from teh user
import smtplib

MY_EMAIL, MY_PASSWORD = '7vkshkumar@gmail.com', 'xxoy lmtd dqmf aqtx'


class SendMail:

    def __init__(self, from_mail, name, msg):
        self.from_mail = from_mail
        self.name = name
        self.message = msg
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login()
