from flask import request, jsonify
from flask_smorest import Blueprint
from flask.views import MethodView
from db import db
from models import Post

post_blp = Blueprint('Posts', 'posts', description='Operations on posts', url_prefix='/post')


# API 리스트
# /post
# 전체 게시글 조회 (GET)
@post_blp.route('/')
class PostList(MethodView):
    def get(self):
        posts = Post.query.all()
        return jsonify([{"post_id": post.post_id,
                         "title": post.title,
                         "content": post.content,
                         "created_at": post.created_at}
                        for post in posts])

    # 새 게시글 생성 (POST)
    def post(self):
        data = request.json
        new_post = Post(  # post_id와 created_at 은 자동 생성 되므로 입력 x
                        title=data["title"],
                        content=data["content"],
                        )
        print(new_post)

        db.session.add(new_post)
        db.session.commit()

        return jsonify({"msg": "Post created successfully"}), 201


# 특정 ID 게시글 조회 (GET)
@post_blp.route('/<int:post_id>')
class PostResource(MethodView):
    def get(self, post_id):
        post = Post.query.get_or_404(post_id)
        return jsonify({"post_id": post.post_id,
                        "title": post.title,
                        "content": post.content,
                        "created_at": post.created_at
                        })

    # 특정 ID를 가진 게시글 수정 (PUT)
    def put(self, post_id):
        post = Post.query.get_or_404(post_id)

        data = request.json

        post.title = data["title"]
        post.content = data["content"]
        # post_id와 created_at 은 생성 되어 있음 -> 입력 x

        db.session.commit()
        return jsonify({"msg": "Post updated successfully"}), 201

    # 특정 ID를 가진 게시글 삭제 (DELETE)
    def delete(self, post_id):
        post = Post.query.get_or_404(post_id)

        db.session.delete(post)
        db.session.commit()

        return jsonify({"msg": "Post deleted successfully"}), 204
