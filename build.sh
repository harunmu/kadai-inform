#!/usr/bin/env bash

# インストール用パッケージ
apt-get update && apt-get install -y wget gnupg curl unzip

# Chrome の公式 GPG キー追加
curl -sSL https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor > /usr/share/keyrings/google-linux-signing-keyring.gpg

# Chrome の apt リポジトリ追加
echo 'deb [signed-by=/usr/share/keyrings/google-linux-signing-keyring.gpg] http://dl.google.com/linux/chrome/deb/ stable main' > /etc/apt/sources.list.d/google-chrome.list

# Chrome インストール
apt-get update && apt-get install -y google-chrome-stable

# Pythonパッケージインストール
pip install -r requirements.txt