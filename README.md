# prototype
## 仕様
### ライブラリをレポジトリ単位で管理するためにweb_appディレクトリにrequirements.txtを配置
- requirements.txtから一括でライブラリインストール
1. cd [web_appディレクトリ]でweb_appに移動
1. pip install -r requirements.txtを実行
* ライブラリを追加する場合は以下
1. pip install [追加したいライブラリ]　でインストール
1. pip freeze > requirements.txt　でrequirements.txtに追加

### SQliteでDBの内容を「DB Browser For Sqlite」で確認する
- 「DB Browser For Sqlite」がインストールされていること前提
1. appディレクトリへ移動
1. sqlite3 db.sqlite3 コマンド実行
1. .output ./dump.txt コマンドで「dump.txt」ファイルを作成（ファイル名は任意）
1. .dump　コマンドで↑で作成したファイルにsql文を保存
1. 「DB Browser For Sqlite」を開き、左上の「File」→「import」→「Database from SQL file」で↑で作成したファイルを指定（ここではdump.txt）
1. 途中で作成されるdbのファイル名を聞かれるが、アプリで設定されているファイル名（デフォルトは「db.sqlite」）にして上書きする
