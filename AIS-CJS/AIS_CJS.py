# selenium Ver : 3.14.1
from selenium import webdriver
# pip install beautifulsoup4
from bs4 import BeautifulSoup as bs

# 웹드라이버 열기 (네이버에 현재상영작 검색 URL)
url = "https://www.catch.co.kr/JobN/Pass/JobReport/05"
driver = webdriver.Chrome()
driver.get(url)

# 크롬드라이버의 현재 페이지의 url 얻기
page_url = driver.page_source
# 현재 url 주소의 html 데이터를 파싱
soup = bs(page_url, "html.parser")
movie_list = soup.find_all(class_='ico next')

# 8개의 영화 정보가 리스트로 저장되어 있습니다.
for movie_info in movie_list:
    print(movie_info.text)