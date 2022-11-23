
def main():
    import requests
    from bs4 import BeautifulSoup
    import time
    import datetime

    # 잡코리아

    f = open('jobkorea_apply_urls.csv', 'w')
    f.write("기업 이름,모집 제목,경력,학력,우대,고용 형태, 급여, 지역, 모집 기간, 이미지 주소" + '\n')

    keyword = "모바일앱"  # 키워드 입력

    # 페이지순서
    for n in range(1, 2):
        raw = requests.get(
            "https://www.jobkorea.co.kr/Search/?stext={}&tabType=recruit&Page_No=".format(keyword) + str(n)
            , headers={'User-Agent': 'Mozilla/5.0'})
        html = BeautifulSoup(raw.text, "html.parser")
        results = html.select("li.list-post")

        for ar in results[0:20]:
            company_name = ar.select_one("a.name").text.strip()
            detail = ar.select_one("a.title").text.strip()
            url = 'https://www.jobkorea.co.kr' + ar.find("a")['href']
            exp = ar.select_one("span.exp").text.strip()
            location = ar.select_one("span.loc").text.strip()
            apply = ar.select_one("div.post-list-apply").text.strip()
            company_name = company_name.replace(",", "")
            detail = detail.replace(",", "")
            location = location.replace(" 외", "")
            now = datetime.datetime.now()
            #nowDate = now.strftime('%Y-%m-%d')
            raw2 = requests.get(url
                                , headers={'User-Agent': 'Mozilla/5.0'})
            html2 = BeautifulSoup(raw2.text, "html.parser")
            #score = str(html2.select("#tab04 > article.artReadStrategy > div > div > div.devStartlist.listArea.specList > div > div.specListWrap > div > ul > li:nth-child(1) > div > span > em"))[5:8]
            date_tag1 = html2.select("#tab02 > div.divReadBx.clear.devMakeSameHeight > article.artReadPeriod > div > dl.date > dd:nth-child(2)")
            date_tag2 = html2.select("#tab02 > div.divReadBx.clear.devMakeSameHeight > article.artReadPeriod > div > dl.date > dd:nth-child(4)")
            prefer_tag = html2.select("#dlPref > dd > span")
            region_tag = html2.select("#container > section > div.readSumWrap.clear > article > div.tbRow.clear > div:nth-child(2) > dl > dd:nth-child(6) > a")
            pay_tag = html2.select("#container > section > div.readSumWrap.clear > article > div.tbRow.clear > div:nth-child(2) > dl > dd:nth-child(4)")
            edu_tag = html2.select("#container > section > div.readSumWrap.clear > article > div.tbRow.clear > div:nth-child(1) > dl > dd:nth-child(4) > strong")
            pattern_tag = html2.select("#container > section > div.readSumWrap.clear > article > div.tbRow.clear > div:nth-child(2) > dl > dd:nth-child(2) > ul > li > strong")
            image_tag = html2.select("#cologo")

            image = ""
            for i in image_tag:
                image = i['src']
            if image == "":
                image = "이미지 없음"
            else:
                image = "http:" + image
            date = ""
            pay = ""
            prefer = ""
            region = ""
            edu = ""
            pattern = ""
            for tag in date_tag1:
                date += "시작일 " + tag.getText() +" "
            for tag in date_tag2:
                date += "마감일 " + tag.getText()
            for tag in prefer_tag:
                prefer += tag.getText()
            for tag in region_tag:
                region += tag.getText()
            for tag in pay_tag:
                pay += tag.getText()
            for tag in edu_tag:
                edu += tag.getText()
            for tag in pattern_tag:
                pattern += tag.getText()

            pay = remove_blank(pay)
            pay = pay.replace(",","")
            region = remove_blank(region)
            prefer = remove_blank(prefer)
            pattern = remove_blank(pattern)
            edu = remove_blank(edu)
            date = remove_blank(date)
            if date == "":
                date = "상시 채용"
            f.write(
                company_name + ',' + detail + ',' + exp + ',' + edu + ',' + prefer + ',' + pattern  + ',' + pay + ',' + region + ',' + date +  ',' + image + '\n')
            time.sleep(1)  # 1초


        print(str(n) + "번째 페이지 내 " + str(keyword) + " 의 채용공고 크롤링을 완료했습니다.")
        print("최종 엑셀 작업 마무리중 입니다.")

    f.close()



    print("잡코리아 크롤링이 완료되었습니다!!")


def remove_blank(string):
    string = string.strip()
    string = string.replace("\n", "")
    string = string.replace("\r", "")
    return string



if __name__ == "__main__":
    main()

