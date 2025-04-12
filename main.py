from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
import uuid
import re
import os
import chromedriver_binary

from datetime import datetime
import time

def scraping():
    # ブラウザの起動

    op = Options()
    op.add_argument('--no-sandbox')  # サンドボックスを無効化
    op.add_argument('--disable-dev-shm-usage')  # 開発用共有メモリの使用を無効化
    # op.add_argument('--disable-extensions')
    op.add_argument('--headless')
    # # op.add_argument(f'--user-data-dir=/dev/shm/selenium_user_data_{uuid.uuid4()}')
    # op.binary_location = '/opt/render/project/src/chromium/chrome'
    op.binary_location = '/opt/render/project/.render/chrome/opt/google/chrome/chrome'
    # service = Service(ChromeDriverManager(version="135.0.7049.84").install())
    browser = webdriver.Chrome(options=op)
    url = 'https://beefplus.center.kobe-u.ac.jp/login'
    browser.get(url)
    sleep(1)

    # ログイン処理

    elem_in = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[3]/div/a")
    elem_in.click()

    elem_id = browser.find_element(By.ID,"username")
    elem_password = browser.find_element(By.ID,"password")
    elem_btn = browser.find_element(By.ID,"kc-login")
    elem_id.send_keys('2355081t')
    elem_password.send_keys('IRK=8urd')
    sleep(1)
    elem_btn.click()

    # 課題ページに移動
    # sleep(1)
    # kadai_btn = browser.find_element(By.XPATH,"/html/body/div[1]/div[1]/span/a")
    # kadai_btn.click()

    # 授業情報ページに移動
    # sleep(1)
    # btn = browser.find_element(By.XPATH,'/html/body/div[1]/div[1]/a[2]')
    # btn.click()

    #テスト
    sleep(1)
    btn = browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[2]/form[1]/div[1]/div[1]/div[4]/div')

    # 日時取得
    sleep(1)
    data = btn.text
    pattern = r'(\d{4})年(\d{2})月(\d{2})日'
    matches = re.findall(pattern,data)
    # year, month, day = matches[1]
    # year, month, day = int(year), int(month), int(day)
    # print(data)
    # data_info = browser.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div[2]/form/div[3]/div[2]/div/div[2]/div[2]/div[5]/span')
    # data_text = data_info.text
    # print(data_text)



    browser.quit()

    # return matches[1]
    submission_date = matches[1]
    subject_day = int(submission_date[2]) - 3
    subject_date_list = list(submission_date)
    subject_date_list[2] = str(subject_day)
    # print(subject_date_list)

    return subject_date_list

if __name__  == "__main__":
    scraping()
    
# submission_date = scraping()
# subject_day = int(submission_date[2]) - 3
# subject_date_list = list(submission_date)
# subject_date_list[2] = str(subject_day)
# print(subject_date_list)
# subject_time_list = ['14', '00', '00']

# subject_date = '-'.join(subject_date_list)
# subject_time = ':'.join(subject_time_list)
# subject_datetime = subject_date + ' ' + subject_time
# subject_obj = datetime.strptime(subject_datetime, "%Y-%m-%d %H:%M:%S")

# now = datetime.now()

# if now < subject_obj:
#         wait_seconds = (subject_obj - now).total_seconds()
#         print(f"指定された日時まで{wait_seconds}秒待機します。")
#         time.sleep(wait_seconds)  # 指定した日時まで待機
#         print('success')


