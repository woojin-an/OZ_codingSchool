from flask import request, jsonify
from flask_smorest import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import Todo, User, db

todo_blp = Blueprint('todo', 'todo',
                     url_prefix='/todo',
                     description='Operations on todos')


# Todo 생성
@todo_blp.route('/', methods=['POST'])
@jwt_required()
def create_todo():
    if not request.is_json:
        return jsonify({'error': 'Missing JSON in request'}), 400

    title = get_jwt_identity()
    if not title:
        return jsonify({"msg": "Missing title"}), 400

    username = get_jwt_identity()
    user = User.query.filter_by(username=username).first()

    new_todo = Todo(title=title, user_id=user.id)
    db.session.add(new_todo)
    db.session.commit()

    return jsonify({"msg": "Todo created", "id": new_todo.id}), 201


# Todo 조회
@todo_blp.route('/<int:todo_id>', methods=['GET'])
@jwt_required()
def get_todos():
    username = get_jwt_identity()
    user = User.query.filter_by(username=username).first()
    todos = Todo.query.filter_by(user_id=user.id).all()
    return jsonify([{
        "id": todo.id,
        "title": todo.title,
        "completed": todo.completed}
        for todo in todos])


# Todo 삭제
@todo_blp.route('/<int:todo_id>', methods=['DELETE'])
@jwt_required()
def delete_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return jsonify({"msg": "Todo deleted", "id": todo_id}), 200