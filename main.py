import datetime
import json

from bs4 import BeautifulSoup
import requests

from linebot import LineBotApi
from linebot.models import TextSendMessage

file = open('info.json', 'r')
info = json.load(file)

CHANNEL_ACCESS_TOKEN = info['CHANNEL_ACCESS_TOKEN']
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

date_today = datetime.date.today()
target_url = f'https://aasj.jp/date/{date_today.year}/{date_today.month:02}/{date_today.day:02}'

r = requests.get(target_url)
soup = BeautifulSoup(r.content, 'html.parser')
target_title = soup.find('h2').get_text()

send_contents = target_title + '\n' + target_url

def main():
    USER_ID = info['USER_ID']
    messages = TextSendMessage(text=send_contents)
    line_bot_api.push_message(USER_ID, messages=messages)
    
if __name__ == "__main__":
    main()