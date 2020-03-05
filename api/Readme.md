## python3をインストール  
brew install python (Mac)  
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

