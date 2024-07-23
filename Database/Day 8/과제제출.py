from pymongo import MongoClient
from datetime import datetime

client = MongoClient('mongodb://localhost:27017/')
db = client.local

# 1. fantasy 장르 책 찾기
def find_books_by_genre(db, genre):
    books_collection = db.books
    query = {
        "genre": genre
        }
    projection = {
        "_id": 0, 
        "title": 1, 
        "author": 1
        }

    books = books_collection.find(query, projection)
    for book in books:
        print(book)

find_books_by_genre(db, "fantasy")

# 2. 감독별 평균 영화 평점 계산
def calculate_average_rating(db):
    movies_collection = db.movies
    pipeline = [
        {
            "$group": {
                "_id": "$director", 
                "average_rating": {"$avg": "$rating"}
                }
            },
        {"$sort": {"average_rating": -1}}
    ]

    results = movies_collection.aggregate(pipeline)
    for result in results:
        print(result)

calculate_average_rating(db)

# 3. 특정 사용자의 최근 행동 조회
def find_recent_actions(db, user_id):
    user_actions_collection = db.user_actions
    query = {
        "user_id": user_id
        }
    sort_criteria = [{"timestamp", -1}]

    actions = user_actions_collection.find(query).sort(sort_criteria).limit(5)
    for action in actions:
        print(action)

find_recent_actions(db, 1)

# 4. 출판 연도별 책의 수 계산
def count_books_by_publication_year(db):
    books_collection = db.books
    pipeline = [
        {
            "$group": {
                "_id": "$year",
                "count": {"$sum": 1}
                }
            },
        {
            "$sort": {"count": 1}
            }
    ]

    results = books_collection.aggregate(pipeline)
    for result in results:
        print(result)

count_books_by_publication_year(db)

# 5. 특정 사용자의 행동 유형 업데이트(2023년 4월 10일 이전의 모든 "view"행동을 "seen"으로 업데이트)
def update_user_action_type_before_date(db, user_id, action, new_action, date):
    user_actions_collection = db.user_actions
    query = {
        "user_id": user_id, 
        "action": action, 
        "timestamp": {"$lt":date}
        }
    update = {"$set": {"action": new_action}}

    result = user_actions_collection.update_many(query, update)
    print(f"updated {result.modified_count} documents")

update_user_action_type_before_date(db, 1, "view", "seen", datetime(2023,4,10))