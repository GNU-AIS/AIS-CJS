from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import sys


# 네이버에서 종목 코드를 불러옴
def search():
    url = "https://www.catch.co.kr/JobN/Pass/JobReport/05"
    wd = webdriver.Chrome()
    wd.get(url)

    # 크롬드라이버의 현재 페이지의 url 얻기
    page_url = wd.page_source
    xpath_button = '//*[@id="report_wrap4"]/div[2]/div[5]/p/a[12]'
    i=0
    wd.find_element(By.XPATH, xpath_button).click()
    time.sleep(1000)
    wd.find_element(By.XPATH, xpath_button).click()
    time.sleep(1000)
    wd.find_element(By.XPATH, xpath_button).click()
    time.sleep(1000)
    wd.find_element(By.XPATH, xpath_button).click()
    time.sleep(1000)
    sys.stdout = open('stdout.txt', 'w', encoding='UTF-8')
    print(wd.page_source)

def main():
    search()


if __name__ == '__main__':
    main()