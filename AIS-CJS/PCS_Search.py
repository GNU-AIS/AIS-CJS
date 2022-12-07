from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
import time
import csv
import json
import sys
import requests

# 네이버에서 종목 코드를 불러옴
def search():
    # 문자열 길이를 저장하는 변수
    company_len = 0
    num = 1
    
    f = open('PCS_Search.csv', 'w')
    f.write("No., 모집 시간, 회사 이름, 분류, 학력, 학과, 학점, 토익, 토스, 오픽, 자격증, 인턴, 대외활동, 해외경험, 수상내역" + '\n')

    # 웹드라이버 열기 (네이버에 현재상영작 검색 URL)
    url = "https://www.catch.co.kr/JobN/Pass/JobReport/05"
    wd = webdriver.Chrome()
    wd.get(url)

    # 크롬드라이버의 현재 페이지의 url 얻기
    xpath_button = '//*[@id="report_wrap4"]/div[2]/div[5]/p/a[12]'
    i=0
    while i < 1:        
        # 크롬드라이버의 현재 페이지의 url 얻기
        page_url = wd.page_source

        # 현재 url 주소의 html 데이터를 파싱
        soup = bs(page_url, "html.parser")
        
        # 데이터 추출 1
        quarter_tag = soup.select('#report_wrap4 > div:nth-child(2) > div:nth-child(5) > div > div:nth-child(1) > div.baseinfo > p.t1')
        company_tag = soup.select('#report_wrap4 > div:nth-child(2) > div:nth-child(5) > div > div:nth-child(1) > div.baseinfo > p.t2 > b')
        field_tag = soup.select('#report_wrap4 > div:nth-child(2) > div:nth-child(5) > div > div:nth-child(1) > div.baseinfo > p.t2')
        Univ_tag = soup.select(
            '#report_wrap4 > div:nth-child(2) > div:nth-child(5) > div > div:nth-child(1) > div.baseinfo > p.t3 > span:nth-child(1)')
        Department_tag = soup.select(
            '#report_wrap4 > div:nth-child(2) > div:nth-child(5) > div > div:nth-child(1) > div.baseinfo > p.t3 > span:nth-child(2)')
        score_tag = soup.select(
            '#report_wrap4 > div:nth-child(2) > div:nth-child(5) > div > div:nth-child(1) > div.rpass_score > dl:nth-child(1) > dd')
        Toeic_tag = soup.select(
            '#report_wrap4 > div:nth-child(2) > div:nth-child(5) > div > div:nth-child(1) > div.rpass_score > dl:nth-child(2) > dd')
        Toss_tag = soup.select(
            '#report_wrap4 > div:nth-child(2) > div:nth-child(5) > div > div:nth-child(1) > div.rpass_score > dl:nth-child(3) > dd')
        Opic_tag = soup.select(
            '#report_wrap4 > div:nth-child(2) > div:nth-child(5) > div > div:nth-child(1) > div.rpass_score > dl:nth-child(4) > dd')
        Certificate_tag = soup.select(
            '#report_wrap4 > div:nth-child(2) > div:nth-child(5) > div > div:nth-child(1) > div.rpass_score > dl:nth-child(5) > dd')
        Intern_tag = soup.select(
            '#report_wrap4 > div:nth-child(2) > div:nth-child(5) > div > div:nth-child(1) > div.rpass_score > dl:nth-child(6) > dd')
        OutAct_tag = soup.select(
            '#report_wrap4 > div:nth-child(2) > div:nth-child(5) > div > div:nth-child(1) > div.rpass_score > dl:nth-child(7) > dd')
        OverExp_tag = soup.select(
            '#report_wrap4 > div:nth-child(2) > div:nth-child(5) > div > div:nth-child(1) > div.rpass_score > dl:nth-child(8) > dd')
        Awards_tag = soup.select(
            '#report_wrap4 > div:nth-child(2) > div:nth-child(5) > div > div:nth-child(1) > div.rpass_score > dl:nth-child(9) > dd')

        for tag in quarter_tag:
            quarter_data = tag.text
        for tag in company_tag:
            company_data = tag.text
        company_len = len(company_data)
        for tag in field_tag:
            field_data = tag.getText()
        field_data = field_data[company_len : len(field_data)]
        for tag in Univ_tag:
            Univ_data = tag.text
        for tag in Department_tag:
            Department_data = tag.text
        for tag in score_tag:
            score_data = tag.text
        for tag in Toeic_tag:
            Toeic_data = tag.text
        for tag in Toss_tag:
            Toss_data = tag.text
        for tag in Opic_tag:
            Opic_data = tag.text
        for tag in Certificate_tag:
            Certificate_data = tag.text
        for tag in Intern_tag:
            Intern_data = tag.text
        for tag in OutAct_tag:
            OutAct_data = tag.text
        for tag in OverExp_tag:
            OverExp_data = tag.text
        for tag in Awards_tag:
            Awards_data = tag.text

        f.write(str(num) + ',' + quarter_data + ',' + company_data + ',' + field_data + ',' + Univ_data + ',' + Department_data + ',' + score_data +
                ',' + Toeic_data + ',' + Toss_data + ',' + Opic_data + ',' + Certificate_data + ',' + Intern_data + ',' + OutAct_data +
                ',' + OverExp_data + ',' + Awards_data + '\n')
        num += 1
        time.sleep(1)  # 0.001초

        # 데이터 추출 2
        quarter_tag = soup.select(
            '#report_wrap4 > div:nth-child(2) > div:nth-child(5) > div > div:nth-child(2) > div.baseinfo > p.t1')
        company_tag = soup.select(
            '#report_wrap4 > div:nth-child(2) > div:nth-child(5) > div > div:nth-child(2) > div.baseinfo > p.t2 > b')
        field_tag = soup.select(
            '#report_wrap4 > div:nth-child(2) > div:nth-child(5) > div > div:nth-child(2) > div.baseinfo > p.t2')
        Univ_tag = soup.select(
            '#report_wrap4 > div:nth-child(2) > div:nth-child(5) > div > div:nth-child(2) > div.baseinfo > p.t3 > span:nth-child(1)')
        Department_tag = soup.select(
            '#report_wrap4 > div:nth-child(2) > div:nth-child(5) > div > div:nth-child(2) > div.baseinfo > p.t3 > span:nth-child(2)')
        score_tag = soup.select(
            '#report_wrap4 > div:nth-child(2) > div:nth-child(5) > div > div:nth-child(2) > div.rpass_score > dl:nth-child(1) > dd')
        Toeic_tag = soup.select(
            '#report_wrap4 > div:nth-child(2) > div:nth-child(5) > div > div:nth-child(2) > div.rpass_score > dl:nth-child(2) > dd')
        Toss_tag = soup.select(
            '#report_wrap4 > div:nth-child(2) > div:nth-child(5) > div > div:nth-child(2) > div.rpass_score > dl:nth-child(3) > dd')
        Opic_tag = soup.select(
            '#report_wrap4 > div:nth-child(2) > div:nth-child(5) > div > div:nth-child(2) > div.rpass_score > dl:nth-child(4) > dd')
        Certificate_tag = soup.select(
            '#report_wrap4 > div:nth-child(2) > div:nth-child(5) > div > div:nth-child(2) > div.rpass_score > dl:nth-child(5) > dd')
        Intern_tag = soup.select(
            '#report_wrap4 > div:nth-child(2) > div:nth-child(5) > div > div:nth-child(2) > div.rpass_score > dl:nth-child(6) > dd')
        OutAct_tag = soup.select(
            '#report_wrap4 > div:nth-child(2) > div:nth-child(5) > div > div:nth-child(2) > div.rpass_score > dl:nth-child(7) > dd')
        OverExp_tag = soup.select(
            '#report_wrap4 > div:nth-child(2) > div:nth-child(5) > div > div:nth-child(2) > div.rpass_score > dl:nth-child(8) > dd')
        Awards_tag = soup.select(
            '#report_wrap4 > div:nth-child(2) > div:nth-child(5) > div > div:nth-child(2) > div.rpass_score > dl:nth-child(9) > dd')

        for tag in quarter_tag:
            quarter_data = tag.text
        for tag in company_tag:
            company_data = tag.text
        company_len = len(company_data)
        for tag in field_tag:
            field_data = tag.getText()
        field_data = field_data[company_len: len(field_data)]
        for tag in Univ_tag:
            Univ_data = tag.text
        for tag in Department_tag:
            Department_data = tag.text
        for tag in score_tag:
            score_data = tag.text
        for tag in Toeic_tag:
            Toeic_data = tag.text
        for tag in Toss_tag:
            Toss_data = tag.text
        for tag in Opic_tag:
            Opic_data = tag.text
        for tag in Certificate_tag:
            Certificate_data = tag.text
        for tag in Intern_tag:
            Intern_data = tag.text
        for tag in OutAct_tag:
            OutAct_data = tag.text
        for tag in OverExp_tag:
            OverExp_data = tag.text
        for tag in Awards_tag:
            Awards_data = tag.text

        f.write(
            str(num) + ',' + quarter_data + ',' + company_data + ',' + field_data + ',' + Univ_data + ',' + Department_data + ',' + score_data +
            ',' + Toeic_data + ',' + Toss_data + ',' + Opic_data + ',' + Certificate_data + ',' + Intern_data + ',' + OutAct_data +
            ',' + OverExp_data + ',' + Awards_data + '\n')
        num += 1
        time.sleep(1)  # 0.001초

        # 버튼을 클릭해 다음 페이지로 넘김
        wd.find_element(By.XPATH, xpath_button).click()
        i += 1


def make_json(csvFilePath, jsonFilePath):
    # create a dictionary
    data = {}

    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        # Convert each row into a dictionary
        # and add it to data
        for rows in csvReader:
            # Assuming a column named 'No' to
            # be the primary key
            key = rows['No.']
            data[key] = rows

    # Open a json writer, and use the json.dumps()
    # function to dump data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))

csvFilePath = r'/Users/hong/PycharmProjects/AIS-CJS/AIS-CJS/PCS_Search.csv'
jsonFilePath = r'/Users/hong/PycharmProjects/AIS-CJS/AIS-CJS/PCS_Search.json'


def main():
    # 정보 추출
    search()
    
    # 정보 json변환
    make_json(csvFilePath, jsonFilePath)


if __name__ == '__main__':
    main()