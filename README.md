# Flask学习记录
## 相关依赖包安装
```
pip install flask==1.1.2
pip install flask_wtf
pip install flask-sqlalchemy
pip install flask-mysqldb
pip install flask_migrate==2.7.0
```
## Migrate
```
python author_book.py db init
python author_book.py db migrate
python author_book.py db upgrade

python author_book.py db migrate -m "add mobile"
python author_book.py db history
python author_book.py db downgrade 版本号
```
## mysql使用sql记录
```
mysql -hlocalhost -uroot -p
create database author_book_py;
use author_book_py;
show tables;
desc tbl_authors;
```