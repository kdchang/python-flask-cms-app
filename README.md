# Python Flask CMS App
This is a Content Management System(CMS) App build by Python Flask.

## Feature
1. Oauth auth / auth
2. CRUD
3. read/write google spreadsheet
4. word.docx

## Usage
1. $ git clone
2. go to venv
3. $ pip install -r requirements.txt
4. $ python manage.py db init
5. $ python manage.py db migrate
6. $ python manage.py db upgrade

## Extensions
1. Flask
2. Flask-SQLAlchemy
3. Flask-Migrate
4. Flask-Script
5. Flsk-Oauthlib
6. mysqlclient
7. python-docx-template
8. gspread
9. gunicorn

## MySQL Setting

if you use linux/ubuntu, please install 

```
$ sudo apt-get install mysql-server
$ sudo apt-get install libmysqlclient-dev
```

setup UTF-8, my.cnf file is located at /etc/mysql/

```
[mysqld]
collation-server = utf8_unicode_ci
init-connect='SET NAMES utf8'
character-set-server = utf8
skip-character-set-client-handshake

[client]
default-character-set   = utf8

[mysql]
default-character-set   = utf8
```

Restart

```
$ sudo service mysql restart
```

1. Enter MySQL
```
$ mysql -u root
```

2. select DB
```
>>> use mysql;
```

3. Update user data and setup root password
```
>>> update user set password=PASSWORD("password") where User='root'; 
```

4. Refresh MySQL
```
>>> flush privileges;
```

5. Exit MySQL
```
>>> quit
```

## DB Migrate
1. Initial
```
$ python manage.py db init
```

2. Add Migration
```
$ python manage.py db migrate
```

3. Update to DB
```
$ python manage.py db upgrade
```

## Documents
1. [flask-oauthlib](https://github.com/lepture/flask-oauthlib/blob/master/example/google.py)
2. [Welcome to python-docx-template’s documentation!](http://docxtpl.readthedocs.io/en/latest/#jinja2-like-syntax)
3. [Mac OS 上安裝 MySQL 以及相關設定筆記](https://www.zeusdesign.com.tw/article/19-Mac%20OS%20%E4%B8%8A%E5%AE%89%E8%A3%9D%20MySQL%20%E4%BB%A5%E5%8F%8A%E7%9B%B8%E9%97%9C%E8%A8%AD%E5%AE%9A%E7%AD%86%E8%A8%98.html)
4. [Install MySQL on macOS Sierra](https://gist.github.com/nrollr/3f57fc15ded7dddddcc4e82fe137b58e)
5. [brew install mysql on mac os el capitan](https://stackoverflow.com/questions/34345726/brew-install-mysql-on-mac-os-el-capitan)
6. [gspread API Reference](http://gspread.readthedocs.io/en/latest/index.html)
7. [Inserting a Python datetime.datetime object into MySQL](https://stackoverflow.com/questions/1136437/inserting-a-python-datetime-datetime-object-into-mysql)
8. [Inserting a unix timestamp into MySQL from Python [duplicate]](https://stackoverflow.com/questions/24367155/inserting-a-unix-timestamp-into-mysql-from-python)
9. [mysql_config not found when installing mysqldb python interface](https://stackoverflow.com/questions/7475223/mysql-config-not-found-when-installing-mysqldb-python-interface)
10. [Change MySQL default character set to UTF-8 in my.cnf?](https://stackoverflow.com/questions/3513773/change-mysql-default-character-set-to-utf-8-in-my-cnf)
11. [ Mysql 插入中文错误：Incorrect string value: '\xE7\xA8\x8B\xE5\xBA\x8F...' for column 'course' at row 1](http://blog.csdn.net/ch717828/article/details/41357431)