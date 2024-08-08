from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests

# driver = webdriver.Chrome()
url = 'https://section.cafe.naver.com/ca-fe/home'

# driver.get(url)
# time.sleep(2)

# html = driver.page_source
req = requests.get(url)
html = req.text
print(html)