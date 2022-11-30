# selenium Ver : 3.14.1
from selenium import webdriver

# 네이버 URL
url = "https:naver.com"
# 네이버 검색창 Xpath
xpath_text = '//*[@id="query"]'
# 검색하기 버튼
xpath_button = '//*[@id="search_btn"]'
# 검색할 내용
keyword = "셀레니움 웹크롤링"


# 웹드라이버 열기
driver = webdriver.Chrome()
driver.get(url)

# 검색 창에 keyword 입력
driver.find_element_by_xpath(xpath_text).send_keys(keyword)
# 검색 버튼 클릭하기기
driver.find_element_by_xpath(xpath_button).click()