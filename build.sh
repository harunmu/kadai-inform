#!/usr/bin/env bash

# インストール用パッケージ
apt-get update && apt-get install -y wget gnupg curl unzip

# Chrome の公式 GPG キー追加
curl -sSL https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor > /usr/share/keyrings/google-linux-signing-keyring.gpg

# Chrome の apt リポジトリ追加
echo 'deb [signed-by=/usr/share/keyrings/google-linux-signing-keyring.gpg] http://dl.google.com/linux/chrome/deb/ stable main' > /etc/apt/sources.list.d/google-chrome.list

# Chrome インストール
apt-get update && apt-get install -y google-chrome-stable

apt-get install -y libxss1 libappindicator3-1 libindicator7

# Pythonパッケージインストール
pip install -r requirements.txt

# # Google Chrome のインストール
# # まず Chocolatey をインストールします (Chocolatey は Windows 用のパッケージマネージャーです)
# Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.SecurityProtocolType]::Tls12; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# # Chocolatey を使って Google Chrome をインストール
# choco install googlechrome -y

# # ChromeDriver のインストール
# # Google Chrome のバージョンを確認して、それに対応する ChromeDriver をダウンロードします
# # 例: ChromeDriver バージョン 134 の場合
# $chromeDriverVersion = '134.0.6998.165' # このバージョンは Google Chrome のバージョンに合わせて変更してください
# Invoke-WebRequest "https://chromedriver.storage.googleapis.com/134.0.6998.165/chromedriver_win32.zip" -OutFile 'C:\Users\harumu.DESKTOP-J6AHOEG\OneDrive\kadai-inform\myproject\chromedriver.exe'
# # Expand-Archive "chromedriver.zip" -DestinationPath "C:\path\to\your\project"

# # Python パッケージインストール
# # 仮想環境を作成して、requirements.txt を使って依存パッケージをインストール
# python -m venv venv
# .\venv\Scripts\activate

# # 依存パッケージのインストール
# pip install -r requirements.txt