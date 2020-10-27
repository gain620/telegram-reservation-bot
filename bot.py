import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pathlib import Path
# import re
# import requests
import telegram

url_list = ['http://www.code-k.co.kr/sub/code_sub04_1.html?R_JIJEM=S3&DIS_T=A']
TELEGRAM_TOKEN = 'xxxxxxxxxxxx'

PROJECT_PATH = Path().absolute()
DRIVER_PATH = Path("{}/driver/chromedriver".format(PROJECT_PATH))
USER_DATA_PATH = Path("{}/driver/UserData".format(PROJECT_PATH))

class ResBot:
    def __init__(self, url_list):
        options = webdriver.ChromeOptions()
        # options.add_argument("start-maximized")
        options.add_argument("--user-data-dir={}".format(USER_DATA_PATH))
        self.browser = webdriver.Chrome(executable_path=DRIVER_PATH, options=options)
        self.browser.implicitly_wait(2)
        self.url_lsit = url_list
        self.MONITOR_INTERVAL = 10

        # 텔레그램 config
        self.bot = telegram.Bot(token=TELEGRAM_TOKEN)
        # supdates = bot.getUpdates()
        # chat_id = updates[-1].message.chat_id

    def __del__(self):
        self.browser.quit()
        print('ResBot Terminated')
        return 1

    def run(self):
        while True:
            for url in self.url_lsit:
                self.browser.get(url)
                elem = self.browser.find_elements(By.CLASS_NAME, 'timeOff')

                if len(elem) > 0:
                    self.bot.sendMessage(chat_id='761691613', text='예약 가능한 시간대 발생')
                    # test = requests.get('https://google.com', verify=False)
                    # print(test.status_code)

                time.sleep(self.MONITOR_INTERVAL)



if __name__=='__main__':
    resBot = ResBot(url_list)
    resBot.run()