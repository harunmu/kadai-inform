import datetime
from email.mime.text import MIMEText
import smtplib

def auto_email(title,message,email_address):

    # メール情報の設定

    from_email = 'rushia0901@gmail.com'
    mail_title = title
    message = message
    to_email = email_address

    # MIMEオブジェクトでメールを作成

    msg = MIMEText(message, 'plain')
    # 第一引数に本文、第二引数にメール形式　(HTML形式の場合 'html')
    msg['Subject'] = mail_title #件名
    msg['To'] = to_email #送信元
    msg['From'] = from_email #宛先

    # サーバー指定

    smtp_host = 'smtp.gmail.com'
    smtp_port = '587'
    smtp_password = 'igtyubqrehudffyt'
    server = smtplib.SMTP(smtp_host,smtp_port)
    # 第一引数でサーバーアドレス、第二引数でポート番号
    server.starttls() #TLSモードでSMPT接続
    server.login(from_email,smtp_password) #暗号化した通信でgmailのsmtpサーバーにログイン
    server.send_message(msg) #メール送信
    server.quit() #接続を終了 


def send_test_email(email_address):
    title = "アカウントは正常に作成されました"
    message = "ご登録ありがとうございます！"

    auto_email(title,message,email_address)

def send_kadai_email(email_address,email_contents,):
    title = "提出期限が近い課題があります"
    message = ""
    for email_content in email_contents:
        message += f"提出 {email_content[0]}日前\n"
        message += f"科目名: {email_content[1]}\n"
        message += f"期限: {email_content[2]}\n\n"
    message += "https://beefplus.center.kobe-u.ac.jp"
    
    auto_email(title,message,email_address)

# if __name__ == '__main__':
#     auto_email()