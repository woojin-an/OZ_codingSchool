import requests
from bs4 import BeautifulSoup

keyword = input("검색어를 하나만 입력하세요:")
url = f"https://www.coupang.com/np/search?component=&q={keyword}&channel=user"

header_user = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36" }
cookie = {"abc" : "abc"}
req = requests.get(url, headers=header_user, cookies=cookie, timeout=3)

html = req.text
soup = BeautifulSoup(html, "html.parser")

items = soup.select("[class=search-product  ]")  # 특정한 클래스의 검색

for rank, item in enumerate(items, 1):
    name = item.select_one(".name").text
    price = item.select_one(".price-value").text
    link = item.a["href"]
    img_src = item.select_one(".search-product-wrap-img")
    rocket = item.select_one(".badge.rocket")

    print("-"*40)
    print(f"순위: {rank}")
    print(f"이름: {name}")
    print(f"가격: {price}")
    print(f"쿠팡 링크: https://www.coupang.com{link}")
    print(f"이미지: http:{img_src.get('data-img-src')}")
    if img_src.get("data-img-src"):
        img_url = f"http:{img_src.get('data-img-src')}"
    else:
        img_url = f"http:{img_src.get('src')}"
    if rocket:
        print("🚀로켓배송 가능")
    else:
        print("로켓배송 불가능")
    img_req = requests.get(img_url)
    with open(f"img/{rank}.jpg", "wb") as f:
        f.write(img_req.content)
print("-"*40)