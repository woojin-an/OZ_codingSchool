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

    title = browser.find_element(By.CLASS_NAME, 'gd_name').text
    author = browser.find_element(By.CLASS_NAME, 'gd_auth').text
    publisher = browser.find_element(By.CLASS_NAME, 'gd_pub').text

    # publishing: 날짜형태
    publishing = browser.find_element(By.CLASS_NAME, 'gd_date').text
    match = re.search(r'(\d+)년 (\d+)월 (\d+)일', publishing)
    if match:
        year, month, day = match.groups()
        date_obj = datetime(int(year), int(month), int(day))
        publishing = date_obj.strftime('%Y-%m-%d')
    else:
        publishing = '2024-01-01'
    
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
    
    try:
        review = browser.find_element(By.CLASS_NAME, 'txC_blue').text
        review = int(review.replace(',', ''))
    except:
        review = 0

    sales = browser.find_element(By.CLASS_NAME, 'gd_sellNum').text.split(" ")[2]
    sales = int(sales.replace(',', ''))

    price = browser.find_element(By.CLASS_NAME, 'yes_m').text[:-1]
    price = int(price.replace(',', ''))

    full_text = browser.find_element(By.CLASS_NAME, 'gd_best').text
    parts = full_text.split(" | ")
    try:
        ranking_part = parts[0]
        ranking = ''.join(filter(str.isdigit, ranking_part))  # 숫자만 추출
    except:
        ranking = 0
    
    try:
        ranking_weeks_part = parts[1]
        ranking_weeks = ''.join(filter(str.isdigit, ranking_weeks_part.split()[-1]))  # 숫자만 추출
    except:
        ranking_weeks = 0

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
