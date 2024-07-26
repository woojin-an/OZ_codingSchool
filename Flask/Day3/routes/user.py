from flask import request, jsonify
from flask_smorest import Blueprint
from flask.views import MethodView
from db import db
from models import User

user_blp = Blueprint("Users", "users", description="Operations on users", url_prefix='/user')

# API List:
# (1) 전체 유저 데이터 조회 (GET)
@user_blp.route('/')
class User_list(MethodView):
    def get(self):
        users = User.query.all()
        user_data = [
            {"id": user.id, "name": user.name, "email": user.email} 
            for user in users
        ]
        return jsonify(user_data)
        
# (2) 유저 생성(POST)
    def post(self):
        data = request.json
        new_user = User(name=data['name'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"msg": "User created successfully"}), 201
    
# (1) 특정 유저 데이터 조회 (GET)
@user_blp.route("/<int:user_id>")
class UserResource(MethodView):
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        print(type(user))

        return jsonify({"id": user.id, "name": user.name, "email": user.email})

# (2) 특정 유저 데이터 업데이트 (PUT)
    def put(self, user_id):
        user = User.query.get_or_404(user_id)
        data = request.json

        user.name = data['name']
        user.email = data['email']

        db.session.commit()
        return jsonify({"msg": "User updated successfully"}), 201
# (3) 특정 유저 삭제 (DELETE)
    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return jsonify({"msg": "User deleted successfully"}), 204