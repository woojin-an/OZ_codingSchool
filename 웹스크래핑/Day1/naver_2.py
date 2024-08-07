import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"}

base_url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query="
keyword = input("검색어를 하나만 입력해주세요")

url = base_url + keyword

req = requests.get(url, header_user)
html = req.text

soup = BeautifulSoup(html, 'html.parser')
# print(soup)

title = soup.select(".title_link")
name = soup.select(".name")

# print(len(title), len(name))

for i in zip(title, name):
    print(f"제목: {i[0].text}")
    print(f"작성자: {i[1].text}")
    print(f"링크: {i[0]['href']}")
    print(f"테스트: {i[0]['class']}")
    print()