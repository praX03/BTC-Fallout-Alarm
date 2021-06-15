import requests
from bs4 import BeautifulSoup
import re
import smtplib
import time
from requests.api import request
import configparser

config = configparser.ConfigParser()
config.read("config.txt")
password = config.get("configuration", "password_token")
sender_email = config.get("configuration", "sender_email")
receiver_email = config.get("configuration", "receiver_email")


def main():
    URL = 'https://in.investing.com/crypto/bitcoin'

    headers = {
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'
    }

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    heading = soup.find(class_="float_lang_base_1 relativeAttr").get_text()
    rate = soup.find(id="last_last").get_text()
    int_rate = re.sub('\D', '', rate)
    int_rate = float(int_rate[0:5])

    alarming_rate = 38000

    if(int_rate <= alarming_rate):
        send_mail(alarming_rate)


def send_mail(alarming_rate):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(sender_email, password)

    subject = 'BTC Rate Alarm!!'
    body = f'Hello from BTC Alarmer!\n BitCoin\'s rate fell down to ${alarming_rate}! This is the most optimal time to buy BTC. All the best!!'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        sender_email,
        receiver_email,
        msg
    )
    print("An E-Mail has been sent")

    server.quit()


while(True):
    main()
    time_interval = 1800
    time.sleep(time_interval)
