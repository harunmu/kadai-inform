from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
from time import sleep
import re
# import os
import chromedriver_binary
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def scraping():

    # ブラウザの起動
    op = Options()
    op.add_argument('--no-sandbox')  # サンドボックスを無効化
    op.add_argument('--disable-dev-shm-usage')  # 開発用共有メモリの使用を無効化
    op.add_argument('--headless')
    op.binary_location = '/opt/render/project/.render/chrome/opt/google/chrome/chrome'
    browser = webdriver.Chrome(options=op)
    url = 'https://beefplus.center.kobe-u.ac.jp/login'
    browser.get(url)

    # ログイン処理
    wait = WebDriverWait(browser, 1)

    elem_in =  wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div/div[1]/div[3]/div/a")))
    elem_in.click()

    elem_id = browser.find_element(By.ID,"username")
    elem_password = browser.find_element(By.ID,"password")
    elem_btn = browser.find_element(By.ID,"kc-login")
    elem_id.send_keys('2355081t')
    elem_password.send_keys('IRK=8urd')
    sleep(1)
    elem_btn.click()

    # 課題ページに移動

    wait = WebDriverWait(browser, 10)

    kadai_btn = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[1]/span/a')))
    kadai_btn.click()

    #課題の詳細を所得
    kadai_list = wait.until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/div[1]/div[2]/div[1]/div[2]/form/div[2]/div[2]/div/div/div[2]/div')))

    class_name_list = []
    kadai_deadline_list = []

    for i,kadai_info in enumerate(kadai_list):
        kadai_deadline_list.append(re.findall(r'\d{4}/\d{2}/\d{2}',kadai_info.text))
        class_name = browser.find_element(By.XPATH,f"/html/body/div[1]/div[2]/div[1]/div[2]/form/div[2]/div[2]/div/div/div[2]/div[{i+1}]/div[1]")
        class_name_list.append(class_name.text)
    
    return class_name_list,kadai_deadline_list,


if __name__  == "__main__":
    scraping()


