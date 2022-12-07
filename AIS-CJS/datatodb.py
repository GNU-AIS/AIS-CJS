import pymysql
from flask import Flask, json, request, jsonify
from threading import Thread
import json, datetime

try:
    app = Flask(__name__)

    @app.route('/corpinput', method=['POST', 'GET'])
    def insert_career():
        conn = pymysql.connect(host='localhost', user='root', password='1234', db='aisprojectdb',
                               charset='utf8')  # mysql 연결
        curs = conn.cursor()

        if conn.open:
            print('corptbl connected')



        with open('json/job.json', encoding='utf-8') as json_file:
            json_data = json.load(json_file)

            i = 0

            for data in json_data:
                print(data)
                name = data.get("company")
                day = data.get("regDt")
                title = data.get("title")
                career = data.get("career")
                education = data.get("minEdubg")
                preference = data.get("prefCd")
                pattern = data.get("empTpCd")
                salary = data.get("minSal")
                area = data.get("basicAddr")
                basicAddr = data.get("wantedInfoUrl")
                time = data.get("holidayTpNm")

        curs.execute("insert into corptbl(name,day,title,career,education,prefernce,pattern,salary,area,basicAddr,time) value (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                     (name,day,title,career,education,preference,pattern,salary,area,basicAddr,time))
        conn.comit()

        conn.close()
except Exception as e:
    print(e)

finally:
    app.run(host='0,0,0,0', port=5050)