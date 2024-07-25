from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import BookSchema

book_blp = Blueprint('books', 'books', url_prefix='/books', description='Operations on books')

# 데이터 저장소(리스트형)
books = []

# 책 목록을 보여주는 GET 엔드포인트
@book_blp.route('/')
class BookList(MethodView):
    @book_blp.response(200, BookSchema(many=True))
    def get(self):
        return books

    # 새 책을 추가하는 POST 엔드포인트    
    @book_blp.arguments(BookSchema)
    @book_blp.response(201, BookSchema)
    def post(self, new_data):
        new_data['id'] = len(books) + 1
        books.append(new_data)
        return new_data

@book_blp.route('/<int:book_id>')
class Book(MethodView):
    #특정 책의 정보를 가져오는 엔트포인트
    @book_blp.response(200, BookSchema)
    def get(self, book_id):
        book = next((book for book in books if book['id'] == book_id), None)
        if book is None:
            abort(404, message="Book not found.")
        return book
    
    #특정 책의 정보를 업데이트
    @book_blp.arguments(BookSchema)
    @book_blp.response(200, BookSchema)
    def put(self, new_data, book_id):
        book = next((book for book in books if book['id'] == book_id), None)
        if book is None:
            abort(404, message="Book not found.")
        book.update(new_data)
        return book
    
    #특정 책을 삭제
    @book_blp.response(204)
    def delete(self, book_id):
        global books
        book = next((book for book in books if book['id'] != book_id), None)
        if book is None:
            abort(404, message="Book not found.")
        books = [book for book in books if book['id'] != book_id]
        return ''