## python3をインストール  
Macの場合，下記のコマンドを実行する．  
```php
brew install python
```  
"brew: command not found" となった場合は，下記のサイトからコマンドをコピペしてHomebrew をインストールする必要あり．  
https://brew.sh/index_ja  
  
* すでにpython2系が入っている場合，下記のコマンドでpython3にアップデートできる．
```php
brew update
```
  
~/.bash_profile に次を記述．    
```php
export PATH=/usr/local/bin:$PATH
alias python="python3"
alias pip="pip3"
```
  
* pathについて困った場合は下記を参照．
https://qiita.com/soarflat/items/d5015bec37f8a8254380  

terminal にて次のコマンドを実行．
```php
source ~/.bash_profile  
```
  
## Djangoのインストール  
下記のコマンドでDjangoおよびDjango REST frameworkをインストール．  
```php
pip install django
pip install djangorestframework
```
  
## runsernerの起動  
```php
python manage.py runserver 192.168.2.105:8000
```
  
## appの作成  
```php
cd {$directory}
mkdir appname
cd ..
python manage.py appname {$directory}/appname
```
  
## Shellの起動  
```php
python manage.py shell
```
