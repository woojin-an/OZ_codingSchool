from selenium import webdriver
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
url = 'https://naver.com'

driver.get(url)
time.sleep(3)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

query = soup.select_one(".search_input_box")
print(query)