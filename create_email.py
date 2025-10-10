import datetime
from email.mime.text import MIMEText
import smtplib

from django.core.mail import send_mail
from django.conf import settings

from_email = settings.DEFAULT_FROM_EMAIL

def send_test_email(email_address):
    title = "アカウントは正常に作成されました"
    message = "ご登録ありがとうございます！"

    message += "アカウント情報の変更はこちら\n"
    message += "https://kadai-inform.onrender.com/account/login/\n"
    
    recipient_list = [email_address]
    
    send_mail(title,message,from_email,recipient_list)

def send_kadai_email(email_address,email_contents,):
    title = "提出期限が近い課題があります"
    message = ""
    for email_content in email_contents:
        message += f"提出 {email_content[0]}日前\n"
        message += f"科目名: {email_content[1]}\n"
        message += f"期限: {email_content[2]}\n\n"

    message += "beef+へのログインはこちら\n"
    message += "https://beefplus.center.kobe-u.ac.jp\n\n"
    message += "アカウント情報の変更はこちら\n"
    message += "https://kadai-inform.onrender.com/account/login/\n"
    
    recipient_list = [email_address]

    send_mail(title,message,from_email,recipient_list)

# if __name__ == '__main__':
#     auto_email()