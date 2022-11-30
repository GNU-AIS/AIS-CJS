from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
import time
import sys
import requests


# 네이버에서 종목 코드를 불러옴
def search():
    f = open('catch.csv', 'w')
    f.write("모집 시간, 회사 이름, 분류, 학력, 학과, 학점, 토익, 토스, 오픽, 자격증, 인턴, 대외활동, 해외경험, 수상내역" + '\n')

    url = "https://www.catch.co.kr/JobN/Pass/JobReport/05"
    response = requests.get(url)

    # 상태체크 "200" : "정상", 정상일 경우 파싱
    if response.status_code == 200:
        html = response.text
        html2 = bs(html, "html.parser")

    time_data = html2.select("#report_wrap4 > div:nth-child(2) > div:nth-child(5) > div > div:nth-child(2) > div.baseinfo")

    wd = webdriver.Chrome()
    wd.get(url)

    # 크롬드라이버의 현재 페이지의 url 얻기
    page_url = wd.page_source
    xpath_button = '//*[@id="report_wrap4"]/div[2]/div[5]/p/a[12]'
    i=0
    data = ""
    while i < 50:
        wd.find_element(By.XPATH, xpath_button).click()
        for tag in time_data:
            data += "시작일 " + tag.getText()
        i += 1
        f.write(data + '\n')

def main():
    search()


if __name__ == '__main__':
    main()