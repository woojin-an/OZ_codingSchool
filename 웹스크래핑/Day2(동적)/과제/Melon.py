from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

user = "Mozilla/5.0 (IPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15(KHTML, like Gecko) CriOS/80.0.3987.95 Mobile/15E148 Safari/604.1"

options_ = Options()
options_.add_argument(f"user-agent={user}")
options_.add_experimental_option("detach", True)
options_.add_experimental_option("excludeSwitches", ["enable-logging"])


#크롬 드라이버 매니저를 자동으로 설치되도록 실행시키는 코드
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options_)

url = "https://m2.melon.com/index.htm"
driver.get(url)
time.sleep(2)
# 이벤트 화면이 있을 시 닫기 기능
try:
    driver.find_element(By.CSS_SELECTOR, ".link-logo").click()
    time.sleep(2)
except Exception as e:
    print(f"Error occurred: {e}")

#  Top100 으로 이동
top100_chart = driver.find_element(By.LINK_TEXT, "멜론차트")
top100_chart.click()
time.sleep(2)

# '더보기' 버튼 클릭 - XPath를 사용하여 onclick 속성이 'hasMore2()'인 버튼 찾기
button = driver.find_element(By.XPATH, "//button[@onclick='hasMore2();']")
button.click()
# print("Button with onclick='hasMore2();' clicked successfully.") # 더보기 버튼 클릭 성공 프린트디버깅
time.sleep(3)  # 페이지 로딩 시간

# html 파싱
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

#아래 순서대로 스크래핑한 자료를 출력해주세요
top100 = soup.select("#_chartList .list_item")

for i in top100:
    # 순위
    rank = i.select_one(".ranking_num").text.strip()
    # 노래 제목
    title = i.select_one(".title.ellipsis").text.strip()
    #가수 이름
    artist = i.select_one(".name.ellipsis").text.strip()

    print("-" * 40)
    print(f"순위: {rank}")
    print(f"노래 제목: {title}")
    print(f"아티스트: {artist}")

print("-"*40)
driver.quit()