import pymysql
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import re
from datetime import datetime
# WebDriver 인스턴스를 생성 (ChromeDriver 경로를 지정하세요)
browser = webdriver.Chrome()
link = 'https://www.yes24.com/Product/Goods/128869414'
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='oz-password',
    db='yes24',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)
with conn.cursor() as cur:
    browser.get(link)
    time.sleep(3)  # 페이지 로드 대기
    try:
        rating_area = browser.find_element(By.CLASS_NAME, 'gd_ratingArea')
        try:
            rating_element = rating_area.find_element(By.CLASS_NAME, 'yes_b')
            rating = rating_element.text
            rating = float(rating.replace(',', '')) if rating else 0.0
        except NoSuchElementException:
            rating = 0.0
    except NoSuchElementException:
        rating = 0.0

    print(f"{rating}")
    # sql = """INSERT INTO Books (
    #     title, author, publisher, publishing, rating, review, sales, price, ranking, ranking_weeks
    #     )
    #     VALUES (
    #     %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
    #     )
    #     """
    # cur.execute(sql, (title, author, publisher, publishing, rating, review, sales, price, ranking, ranking_weeks))
    # conn.commit()
    # time.sleep(3)  # 다음 링크로 넘어가기 전 대기

# WebDriver 종료
browser.quit()

# 데이터베이스 연결 종료
conn.close()
