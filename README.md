# 論文紹介サイト通知プログラム

## はじめに

<strong>このプログラムは個人的な使用を目的としており、その結果に対する責任は負いかねます。</strong>

<strong>また、現在は本プログラムを使用していないので、動作確認はしていません。</strong>

詳しくは`注意事項`をお読みください。

## プロジェクトの目的

このプログラムは、論文を読む機会を増やすために作成しました。

特定のサイトから記事のタイトルとURLをスクレイピングし、それをLineBotを通じて通知することで、<br>
論文に触れる機会を増やすことができます。

こちらのサイトが通知されます：https://aasj.jp/watch.html

![ScreenShot 2022-10-16 23 50 08](https://user-images.githubusercontent.com/86920995/196042238-7a8f0341-abd7-40d1-ba94-529acbb76c73.JPG)


## 主な機能

- 論文情報の自動収集: 特定のウェブサイトから毎日の論文情報をスクレイピング。
- Line通知: 収集した論文情報をLineを通じて通知。
- GitHub Actionsによる定期実行: 定期的にスクリプトを実行し、常に最新の情報を提供

## 技術スタック

- Web scraping: Pythonを使用したウェブスクレイピング。
- Messeaging API: LineのMessaging APIを使用して通知を送信。
- GitHub Actions: 定期的なスクリプト実行の自動化。

## セットアップ

### 動作確認環境

- Ubuntu 22.04
- Python 3.10

### 使い方

1. 依存関係のインストール: 必要なライブラリをインストールします。

```python

pip install --upgrade pip

pip install -r requirements.txt

```

2. Line Messaging APIの設定: Line Developer ConsoleでBotを設定し、必要なトークンを取得します。

3. info.jsonの設定: 取得したトークンをinfo.jsonに組み込みます。

## カスタマイズ方法

`extract_article_info` メソッドの戻り値を変更することで、送信する内容をカスタマイズできます。

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

## 注意事項

### ウェブスクレイピングの倫理と法的規制

- 利用規約の遵守: 対象ウェブサイトの利用規約を必ず確認し、遵守してください。

- アクセス頻度の制限: サイトへのアクセス頻度を適切に制限し、サーバーへの負荷を最小限に抑えてください。

- データの取り扱い: 収集したデータは個人的な使用に限定し、著作権やプライバシーの問題を避けるために第三者と共有しないようにしてください。

### プログラムの使用に関する免責事項

- データの正確性: このプログラムはウェブサイトからの情報を自動的に収集しますが、収集されたデータの完全性や正確性については保証しません。

- 利用のリスク: このプログラムの使用によって生じるいかなる損害や問題についても、開発者は責任を負いかねます。<br>
  利用者は自己の責任の下でプログラムを使用することを理解してください。

- 更新とサポート: このプログラムは個人的なプロジェクトとして開発されており、定期的な更新やサポートを保証するものではありません。<br>
  将来的に機能が変更される可能性があります。

### セキュリティに関する注意

- APIキーの管理: 使用するAPIキーは適切に管理してください。
