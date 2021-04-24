# 쿠팡에서 노트북 검색 후 평점, 리뷰가 많은 제품 추출하기

import requests
import re
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"}


# 페이지 변환 자동 처리
for i in range(1,6):
    print("pages:", i)
    # url page에 i로 변경하기 - {}    .format(i)
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=4&backgroundColor=".format(i)




    res = requests.get(url, headers = headers)
    res.raise_for_status()

    #res.text를 lxml 파서를 통해 BS 객체로 변경함
    soup = BeautifulSoup(res.text, 'lxml')

    #li tag 가운데, class 가운데 search-product인 모든 것을 추출
    items = soup.find_all("li", attrs = {"class" : re.compile("^search-product")})
    # print(items[0].find("div", attrs = {"class" : "name"}).get_text())
    #노트북의 상품명, 가격, 평점, 평점수 추출

    for item in items:
        #광고 제품 제거
        ab_badge = item.find("span", attrs = {"class":"ad-badge-text"})
        if ab_badge:
            # print("No Ad Product")
            continue

        name = item.find("div", attrs = {"class" : "name"}).get_text() #제품명

        #애플 제품 제외
        if "Apple" in name:
            # print("Apple 제품 제외")
            continue

        price = item.find("strong", attrs = {"class" : "price-value"}).get_text()#가격

        #리뷰 100개 이상, 평점 4.5 이상만 추출
        rate = item.find("em", attrs = {"class" : "rating"})

        if rate:
            rate = rate.get_text()
        else:
            # print("평점 없는 상품 제외")
            continue
        rate_cnt = item.find("span", attrs = {"class" : "rating-total-count"})

        if rate_cnt:
            rate_cnt = rate_cnt.get_text()[1:-1]
            # print("리뷰수", rate_cnt)
        else:
            # rate_cnt = "No Rate CNT"
            print("평점수 없는 상품 제외")
            # continue

        link = item.find("a", attrs = {"class":"search-product-link"})["href"]

        if float(rate) >= 4.5 and int(rate_cnt) >= 100:#괄호 부분 제거
            # print(name, price, rate, rate_cnt)
            print(f"name: {name}")
            print(f"price: {name}")
            print(f"rate: {rate} 점 ({rate_cnt}개)")
            print("link: {}".format("https://www.coupang.com" + link))
            print(f"-"*100) # 줄긋기



