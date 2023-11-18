# 論文紹介サイト通知プログラム

論文を読む機会を増やすために、LineBotAPIを使って論文紹介サイトのURLが通知されるプログラムを作りました。

個人用に作ったので参考程度に使用してください。

![ScreenShot 2022-10-16 23 50 08](https://user-images.githubusercontent.com/86920995/196042238-7a8f0341-abd7-40d1-ba94-529acbb76c73.JPG)

こちらのサイトが通知されます：https://aasj.jp/watch.html

## 作成に使用したもの

- Web scraping
- Messeaging API
- GitHub Actions

GitHub Actionsで定期実行されるようにしています。

※現在は使用していないのでGitHub Actionsの動作確認はしていません。

## 動作確認済みの環境

- Ubuntu 22.04
- Python 3.10

## カスタマイズ方法

以下のメソッドの戻り値を変更することで、送信する内容をカスタマイズできます。

メソッドの戻り値はstringsを想定しています。

<strong>スクレイピングで記事を取得する場合、対象のサイトの規約や、サイトに負荷をかけないよう十分注意してください。</strong>

参考記事：https://hnavi.co.jp/knowledge/blog/scraping-development/#title6

```
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
```
