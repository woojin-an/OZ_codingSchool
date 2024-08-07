import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"}

base_url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query="
keyword = input("검색어를 하나만 입력해주세요")

url = base_url + keyword

req = requests.get(url, header_user)
html = req.text

soup = BeautifulSoup(html, 'html.parser')

wraps = soup.select(".view_wrap")

# 클래스를 통해서 하나의 정보만 가져올때는 select_one
# 클래스를 통해서 해당하는 모든 정보를 가져올때는 select
# 클래스는 " . " 를 이용하여 구분
print("==========================================================================")
print(f"검색 키워드: {keyword}")
for i in wraps:
    ad = i.select_one(".spblog.ico_ad")
    if not ad:
        title = i.select_one(".title_link")
        name = i.select_one(".name")
        print()
        print(f"제목: {title.text}")
        print(f"작성자: {name.text}")
        print(f"링크: {title['href']}")
        

print("==========================================================================")
