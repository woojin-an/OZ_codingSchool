# 멜론 사이트에서 Top 100 가져오기

# 순위
# 제목 : 정보
# 가수 :
# 앨범제목
import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"}

base_url = "https://www.melon.com/chart/index.htm?dayTime="

# 날짜 입력
url_date = input("날짜를 8자리로 입력해주세요 (형식: YYYYMMDD): ")
if len(url_date) != 8 or not url_date.isdigit():
    print("날짜는 8자리 숫자로 입력해주세요.")
    exit()

# 시각 입력
url_time = input("시각을 입력해주세요 (형식: HH): ")
if len(url_time) != 2 or not url_time.isdigit():
    print("시각은 2자리 숫자로 입력해주세요.")
    exit()
if not (0 <= int(url_time) <= 23):
    print("시각은 00부터 23 사이의 숫자여야 합니다.")
    exit()

url = base_url + url_date + url_time

req = requests.get(url, headers=header_user)
html = req.text


soup = BeautifulSoup(html, 'html.parser')

wraps_50 = soup.select(".lst50")
wraps_100 = soup.select(".lst100")
wraps = wraps_50 + wraps_100

print(f"{url_date[0:4]}년 {url_date[4:6]}월 {url_date[6:]}일 {url_time}시의 Top100 입니다")

for i in wraps:
    rank = i.select_one(".rank").text.strip()
    title = i.select_one(".ellipsis.rank01").text.strip()
    artist = i.select_one(".checkEllipsis").text.strip()
    album = i.select_one(".ellipsis.rank03").text.strip()
    print("-" * 40)
    print(f"순위: {rank}")
    print(f"제목: {title}")
    print(f"가수: {artist}")
    print(f"앨범: {album}")

print("-" * 40)
