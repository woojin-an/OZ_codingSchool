from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
# 클래스, 아이디, css_selector 를 이용하고자 할 때
from selenium.webdriver.common.by import By
# 키보드로 입력할 수 있는 기능 제공
from selenium.webdriver.common.keys import Keys
import time

header_user = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"

options = Options()
options.add_argument(f"User-Agent={header_user}")  # 헤더 유저 값 넣어주는 옵션
options.add_experimental_option("detach", True)  # 브라우저 종료되지 않게 하는 옵션
options.add_experimental_option("excludeSwitches", ["enable-logging"])  # 브라우저 상단 '자동화' 문구 삭제

#  브라우저 접속
driver = webdriver.Chrome()
url = "https://kream.co.kr"
driver.get(url)
time.sleep(1)

#  검색창으로 이동
driver.find_element(By.CSS_SELECTOR, ".btn_search").click()
time.sleep(1)

#  이동한 검색창에 키워드 입력
driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys("슈프림")
time.sleep(1)

#  검색어 입력시킨 후 엔터 입력
driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys(Keys.ENTER)
time.sleep(1)

#  페이지 스크롤
for i in range(10):
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)  # pagedown 키를 이용
    time.sleep(0.5)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

#  제품 별 정보 추출 준비 (item_inner)
items = soup.select(".item_inner")

product_list = []

for i in items:
    product_name = i.select_one(".translated_name").text
    if "후드" in product_name:
        category = "상의"
        product_brand = i.select_one(".product_info_brand.brand").text
        # product_name_hood = i.select_one(".translated_name").text
        product_price = i.select_one(".amount").text

        print(category, product_brand, product_name, product_price)
# 브랜드

# 제품명

# 가격

# 거래량

#  브라우저 종료
driver.quit()