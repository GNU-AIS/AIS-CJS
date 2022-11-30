from bs4 import BeautifulSoup
from selenium import webdriver
import time
import sys


# 네이버에서 종목 코드를 불러옴
def search():
    url = "https://www.catch.co.kr/JobN/Pass/JobReport/05"
    wd = webdriver.Chrome('./WebDriver/chromedriver.exe')
    '''wd = webdriver.Chrome('C:/Users/hong/Desktop/chromedriver_win32/chromedriver.exe')'''

    wd.get(url)
    xpath_button = '//*[@id="report_wrap4"]'
    wd.find_element_by_link_text(xpath_button).click()
    time.sleep(10)

    sys.stdout = open('stdout.txt', 'w', encoding='UTF-8')
    print(wd.page_source)

def main():
    search()


if __name__ == '__main__':
    main()