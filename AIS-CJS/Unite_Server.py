import pymysql
from flask import Flask, json, request, jsonify
from threading import Thread
import json, datetime

try:
    app = Flask(__name__)


    @app.route('/corpoutput', methods=['POST', 'GET'])
    def corpdboutput():
        conn = pymysql.connect(host='localhost', user='root', password='1234', db='aisprojectdb',
                               charset='utf8')  # mysql 연결
        curs = conn.cursor()

        if conn.open:
            print('corptbl connected')

        sql = "select * from corptbl"
        curs.execute(sql)
        rows = curs.fetchall()
        columns = [desc[0] for desc in curs.description]
        result = []
        for row in rows:
            row = dict(zip(columns, row))
            result.append(row)
        row = result

        conn.close()
        return row

    @app.route('/careeroutput', methods=['POST', 'GET'])
    def careerdboutput():
        conn = pymysql.connect(host='localhost', user='root', password='1234', db='aisprojectdb',
                               charset='utf8')  # mysql 연결
        curs = conn.cursor()

        if conn.open:
            print('careertbl connected')

        sql = "select * from careertbl"
        curs.execute(sql)
        rows = curs.fetchall()
        columns = [desc[0] for desc in curs.description]
        result = []
        for row in rows:
            row = dict(zip(columns, row))
            result.append(row)
        row = result

        conn.close()
        return row


    @app.route('/corpinput', methods=['GET'])
    def insert_corp():
        conn = pymysql.connect(host='localhost', user='root', password='1234', db='aisprojectdb',
                               charset='utf8')  # mysql 연결
        curs = conn.cursor()

        if conn.open:
            print('corptbl connected for insert')

        k = 1
        curs.execute("truncate corptbl")

        for i in range(1,11):
            json_file = "json/corp/job" + str(i) + ".json"
            json_data = open(json_file).read()
            json_obj = json.loads(json_data)

            for data in json_obj:
                name = data.get("company")
                day = data.get("closeDt")
                title = data.get("title")
                career = data.get("career")
                education = data.get("minEdubg")
                preference = data.get("prefCd")
                pattern = data.get("empTpCd")
                salary = data.get("minSal")
                area = data.get("basicAddr")
                basicAddr = data.get("wantedInfoUrl")
                time = data.get("holidayTpNm")

                curs.execute(
                    "insert into corptbl(k,name,day,title,career,education,preference,pattern,salary,area,basicAddr,time) value (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (k,name, day, title, career, education, preference, pattern, salary, area, basicAddr, time))
                k += 1

        conn.commit()
        conn.close()

        print("기업 공고 데이터 삽입 완료")

        return json_obj

    @app.route('/careerinput', methods=['GET'])
    def insert_career():
        conn = pymysql.connect(host='localhost', user='root', password='1234', db='aisprojectdb',
                               charset='utf8')  # mysql 연결
        curs = conn.cursor()

        if conn.open:
            print('careertbl connected for insert')

        json_data = open("json/career/PCS_Search.json").read()
        json_obj = json.loads(json_data)

        curs.execute("truncate careertbl")

        for data in json_obj:
            key = data.get("No.")
            corp_name = data.get("\ud68c\uc0ac \uc774\ub984")
            time = data.get("\ubaa8\uc9d1 \uc2dc\uac04")
            credit = data.get("\ud559\uc810")
            toeic = data.get("\ud1a0\uc775")
            toeic_sp = data.get("\ud1a0\uc2a4")
            opic = data.get("\uc624\ud53d")
            certificate = data.get("\uc790\uaca9\uc99d")
            intern =  data.get("\uc778\ud134")
            external_activities = data.get("\ub300\uc678\ud65c\ub3d9")
            overseas_study = data.get("\ud574\uc678\uacbd\ud5d8")
            awards = data.get("\uc218\uc0c1\ub0b4\uc5ed")
            major = data.get("\ud559\uacfc")
            university = data.get("\ud559\ub825")

            curs.execute("insert into careertbl(pk,corp_name,time,credit,toeic,toeic_sp,opic,certificate,intern,external_activities,overseas_study,awards,major,university) value (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                        , (key,corp_name,time,credit,toeic,toeic_sp,opic,certificate,intern,external_activities,overseas_study,awards,major,university))

        conn.commit()
        conn.close()
        print("합격자 스펙 데이터 삽입 완료")

        return json_obj

except Exception as e:
    print(e)

finally:
    app.run(host='0.0.0.0', port=5000)
