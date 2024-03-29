import datetime
import json

from bs4 import BeautifulSoup
import requests

from linebot import LineBotApi
from linebot.models import TextSendMessage


INFO_PATH = './info.json'


class ArticleLinkSender(object):

    def __init__(self, info_path: str):
        # ラインボットに必要な情報を読み込む
        info = self.load_info(info_path)

        self.user_id = info['user_id']
        self.line_bot_api = LineBotApi(info['channel_access_token'])

    def send_messages(self, contents: str):
        messages = TextSendMessage(text=contents)
        self.line_bot_api.push_message(self.user_id, messages=messages)

    @staticmethod
    def load_info(file_path: str):
        with open(file_path) as f:
            info = json.load(f)

        for iv in info.values():
            if len(iv) == 0:
                raise ValueError('必要な情報がありません')

        return info


    @staticmethod
    def extract_article_info() -> str:
        today = datetime.date.today()
        url = f'https://aasj.jp/date/{today.year}/{today.month:02}/{today.day:02}'

        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')

        title = soup.find('h2').get_text()

        if (title is None) | (len(title) == 5):
            return '記事を取得できませんでした'

        else:
            return title + '\n' + url


def main():
    sender = ArticleLinkSender(INFO_PATH)
    contents = sender.extract_article_info()
    sender.send_messages(contents)


if __name__ == "__main__":
    main()
