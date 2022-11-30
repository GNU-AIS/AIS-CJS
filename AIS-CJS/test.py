from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import sys


def main():
    url = "https://www.catch.co.kr/JobN/Pass/JobReport/05"
    chrome_options = webdriver.ChromeOptions()
    wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    wd.get(url)
    xpath_button = '//*[@id="report_wrap4"]/div[2]/div[5]/p/a[12]'
    #wd.find_element_by_link_text(xpath_button).click()
    wd.find_element(xpath_button, "다음").click()
    time.sleep(1000)

    sys.stdout = open('stdout.txt', 'w', encoding='UTF-8')
    print(wd.page_source)


if __name__ == '__main__':
    main()
