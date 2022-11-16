import pymysql
from flask import Flask

conn = pymysql.connect(host='localhost', user='root', password='1234', db='BBS', charset='utf8') # mysql 연결
curs = conn.cursor() # sql 문 입력용 cursor 생성

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World"