import datetime
from datetime import timedelta,datetime
import schedule
from time import sleep
from email.mime.text import MIMEText
import smtplib
# from sel import content_sub,dead_line


# content = sel.output()

def auto_email():




    # メール情報の設定

    from_email = 'rushia0901@gmail.com'
    to_email = 'rushia0901@gmail.com'
    mail_title = "h"
    message = "科目:" +" 期限：" 

    # MIMEオブジェクトでメールを作成

    msg = MIMEText(message, 'plain')
    # 第一引数に本文、第二引数にメール形式　(ＨＴＭＬ形式の場合 'html')
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

if __name__ == '__main__':
    auto_email()

# 指定の時刻に処理を行う

# for ctn in dead_line:
#     data =datetime.strptime(ctn.text, "%Y/%m/%d %H:%M:%S")
#     print(data)

# today = datetime.now()
# for ctn in dead_line:
#     data =datetime.strptime(ctn.text, "%Y/%m/%d %H:%M:%S")
#     if(today<data):
#         auto_email()

        

# schedule.every().days.at("12:40").do(auto_email)

# while True:
#     schedule.run_pending()
#     sleep(1) 