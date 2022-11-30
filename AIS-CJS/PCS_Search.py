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

    # 웹드라이버 열기 (네이버에 현재상영작 검색 URL)
    url = "https://www.catch.co.kr/JobN/Pass/JobReport/05"
    wd = webdriver.Chrome()
    wd.get(url)













    # 크롬드라이버의 현재 페이지의 url 얻기
    xpath_button = '//*[@id="report_wrap4"]/div[2]/div[5]/p/a[12]'
    i=0
    while i < 1:
        wd.find_element(By.XPATH, xpath_button).click()
        i += 1


        # 크롬드라이버의 현재 페이지의 url 얻기
        page_url = wd.page_source

        # 현재 url 주소의 html 데이터를 파싱
        soup = bs(page_url, "html.parser")
        quarter_tag = soup.select(
            '#report_wrap4 > div:nth-child(2) > div:nth-child(5) > div > div:nth-child(2) > div.baseinfo > p.t1')
        company_tag = soup.select('#report_wrap4 > div:nth-child(2) > div:nth-child(5) > div > div:nth-child(2) > '
                                  'div.baseinfo > p.t2 > b')
        field_tag = soup.select('#report_wrap4 > div:nth-child(2) > div:nth-child(5) > div > div:nth-child(2) > div.baseinfo > p.t2')

        # 8개의 영화 정보가 리스트로 저장되어 있습니다.
        for tag in quarter_tag:
            quarter_data = tag.text
        for tag in company_tag:
            company_data = tag.text
        for tag in field_tag:
            field_data = tag.getText()

        f.write(quarter_data + ',' + company_data + ',' + field_data +'\n')
        time.sleep(1)  # 1초

def main():
    search()


if __name__ == '__main__':
    main()