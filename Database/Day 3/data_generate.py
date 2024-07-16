import mysql.connector
from faker import Faker
import random #파이썬 기본 모듈

# (1) MySQL 연결 설정
db_connection = mysql.connector.connect(
    host="localhost",
    user="root", # MySQL user
    password="oz-password", # MySQL password
    database="testdatabase" # MySQL database name
)

# (2) MySQL 연결
cursor = db_connection.cursor()
faker = Faker()

# users 데이터 생성
for _ in range(100):
    username = faker.user_name()
    print(username)