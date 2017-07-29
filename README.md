# Python Flask CMS App

## Feature
1. Oauth auth
2. CRUD
3. read/write google doc / word / spreadsheet

## Usage
1. $ git clone
2. go to venv
3. $ pip install -r requirements.txt
4. $ python manage.py db init
5. $ python manage.py db migrate

## Extensions
1. Flask
2. Flask-SQLAlchemy
3. Flask-Migrate
4. Flask-Script
5. Flsk-Oauthlib
6. mysqlclient
7. python-docx-template

## MySQL Setting

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

## Documents
1. [flask-oauthlib](https://github.com/lepture/flask-oauthlib/blob/master/example/google.py)
2. [Welcome to python-docx-template’s documentation!](http://docxtpl.readthedocs.io/en/latest/#jinja2-like-syntax)
3. [Mac OS 上安裝 MySQL 以及相關設定筆記](https://www.zeusdesign.com.tw/article/19-Mac%20OS%20%E4%B8%8A%E5%AE%89%E8%A3%9D%20MySQL%20%E4%BB%A5%E5%8F%8A%E7%9B%B8%E9%97%9C%E8%A8%AD%E5%AE%9A%E7%AD%86%E8%A8%98.html)
4. [Install MySQL on macOS Sierra](https://gist.github.com/nrollr/3f57fc15ded7dddddcc4e82fe137b58e)
5. [brew install mysql on mac os el capitan](https://stackoverflow.com/questions/34345726/brew-install-mysql-on-mac-os-el-capitan)