import requests
from bs4 import BeautifulSoup

header_user = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}

base_url = "http://www.cgv.co.kr/movies/?lt=1&ft=0"

# 요청 및 HTML 파싱
req = requests.get(base_url, headers=header_user)
html = req.text
soup = BeautifulSoup(html, 'html.parser')

# 데이터 추출
wraps = soup.select(".sect-movie-chart")

for wrap in wraps:
    rank = wrap.select(".box-image")
    contents = wrap.select(".box-contents")

    for rank, contents in zip(rank, contents):
        
        # 순위
        rank_text = rank.find('strong', class_='rank').get_text(strip=True)
        rank_text = rank_text[3::] # 출력물 slicing
        # 제목
        title = contents.find('strong', class_='title').get_text(strip=True)
        # 예매율
        reserve_rate = contents.find('strong', class_='percent').get_text(strip=True)
        reserve_rate = reserve_rate[3::] # 출력물 slicing
        # 개봉일자
        open_date = contents.find('span', class_='txt-info').get_text(strip=True)
        open_date = open_date[0:10] # 출력물 slicing
        
        print("=" * 40)  # 구분선
        print(f"순위: {rank_text}위")
        print(f"제목: {title}")
        print(f"예매율: {reserve_rate}")
        print(f"개봉일: {open_date}")
print("=" * 40)  # 구분선
