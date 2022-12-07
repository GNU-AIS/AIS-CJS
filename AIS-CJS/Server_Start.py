import pymysql
from flask import Flask, json, request, jsonify
from threading import Thread
import datetime, json


conn = pymysql.connect(host='localhost', user='root', password='1234', db='aisprojectdb', charset='utf8') # mysql 연결
curs = conn.cursor() # sql문을 입력할 cursor 생성

if conn.open: # DB 연결 여부
    print('connected')

try:
    app = Flask(__name__)
    # flask 메인 
    # __name__: 현재 이 파일을 실행하고 있는 파일의 이름이 들어감(원본과 같은 파일 일 경우 '__main__')

    #Career Output
    #@app.route('/careeroutput',methods=['POST','GET'])

   # def careerdboutput(): # DB에서 웹으로 데이터를 보내기위한 함수

     #   sql = "select * from careertbl" # DB에서 필요한 데이터 select하는 sql문
     #   curs.execute(sql) # sql문 실행
     #   rows = curs.fetchall() # select한 데이터 fetch (fetchall() : 모든 데이터 fetch)
    #    columns = [desc[0] for desc in curs.description]
    #    result = []
    #    for row in rows:
    #        row = dict(zip(columns, row))
    #        result.append(row)
    #    row = result
    #    return row
        # fetch한 데이터 json형식으로 변환 후 string으로 바꿔서 return

    @app.route('/corpoutput',methods=['POST', 'GET'])

    def corpdboutput():
        sql = "select * from corptbl"
        curs.execute(sql)
        rows = curs.fetchall()
        columns = [desc[0] for desc in curs.description]
        result = []
        for row in rows:
            row = dict(zip(columns, row))
            result.append(row)
        row = result
        return row

    # @app.route('/careerinput',methods=['POST', 'GET'])
    #
    # @app.route('/corpinput',methods=['POST','GET'])
    #
    # def jsontodb():
    #    company = request.json('company')
    #    #busino = request.json('busino')
    #    title = request.json('title')
    #    #salTpNm = request.json('salTpNm')
    #    salary = request.json('minSal')
    #    #maxSal = request.json('maxSal')
    #    area = request.json('region')
    #    time = request.json('holidayTpNm')
    #    education = request.json('minEdubg')
    #    #maxEdubg = request.json('maxEdubg')
    #    career = request.json('career')
    #    #regDt = request.json('regDt')
    #    day = request.json('closeDt')
    #    basicAddr = request.json('wantedInfoUrl')
    #    #wantedMobileInfoUrl = request.json('wantedMobileInfoUrl')
    #    #basicAddr = request.json('basicAddr')
    #    pattern = request.json('empTpCd')
    #    #jobsCd = request.json('jobsCd')
    #    #smodifyDfm = request.json('smodifyDfm')
    #    preference = request.json('prefCd')
    #
    #    return "Success"
except Exception as e:
    print(e)


finally:
    app.run(host='0.0.0.0', port= 5000)
    conn.close()