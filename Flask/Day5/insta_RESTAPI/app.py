from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

users = [
    {
        "username": "leo",
        "posts": [{"title": "Town House", "likes": 120}]
    },
    {
        "username": "alex",
        "posts": [{"title": "Mountain Climbing", "likes": 350}, {"title": "River Rafting", "likes": 200}]
    },
    {
        "username": "kim",
        "posts": [{"title": "Delicious Ramen", "likes": 230}]
    }
]


# 모든 사용자 조회
@app.route("/")
def index():
    return render_template('index.html')


# 사용자 조회
@app.route("/users")
def get_users():
    return {"users": users}


# 사용자 추가
@app.route("/users")
def create_user():
    request_data = request.get_json()
    new_user = {
        "username": request_data["username"],
        "posts": request_data[{"title": "content", "likes": 0}]
    }
    users.append(new_user)
    return new_user, 201


# 게시물 추가
@app.route("/")
def add_post(username):
    request_data = request.get_json()
    for user in users:
        if user["username"] == username:
            new_post = {
                "title": request_data["title"],
                "likes": request_data["likes"]
            }
            user["posts"].append(new_post)
            return new_post, 201


# 사용자별 게시물 조회
@app.route("/users")
def get_post_of_user(username):
    request_data = request.get_json()
    for user in users:
        if user["username"] == username:
            return {"posts": user["posts"]}
    return {"msg": "User not found"}, 404


# 특정 게시물의 좋아요 수 증가
@app.route("/users")
def increase_post_of_user(username, title):
    for user in users:
        if user["username"] == username:
            for post in user["posts"]:
                if post["title"] == title:
                    post["likes"] += 1
                    return post
            return {"msg": "Post not found"}, 404
    return {"msg": "User not found"}, 404


# 사용자 삭제
@app.route("/users/<string:username>")
def delete_user(username):
    global users
    users = [user for user in users if user["username"] != username]
    return {"msg": "User deleted"}, 200


if __name__ == "__main__":
    app.run(debug=True)
