from flask_smorest import Blueprint, abort
from schemas import BookSchema
from flask.views import MethodView

blp = Blueprint('books', 'books', 
                url_prefix='/books', 
                description='Operations on books')

# 데이터 저장소
books = []

# BookList 클래스 - GET 및 POST 요청을 처리
@blp.route('/')
class BookList(MethodView):
    @blp.response(200)
    def get(self):
        # 모든 아이템을 반환하는 GET 요청 처리
        return books
    
    @blp.arguments(BookSchema)
    @blp.response(201, description='Book added')
    def post(self, new_data):

        books.append(new_data)
        return new_data
    
    # Book 클래스 - GET, PUT, DELETE 요청을 처리
    @blp.route("/<int:book_id>")
    class Book(MethodView):
        @blp.response(200)
        def get(self, book_id):
            book = next((book for book in books if book['id'] == book_id), None)
            if book is None:
                abort(404, message="Book not found")
            return book
        
    @blp.arguments(BookSchema)
    @blp.response(200, description="Book updated")
    def put(self, new_data, book_id):
        book = next((book for book in books if book['id'] == book_id), None)
        if book is None:
            abort(404, message="Book not found")
        book.update(new_data)
        return book

    @blp.response(204, description="Book deleted")
    def delete(self, book_id):
        global books
        if not any(book for book in books if book["id"] == book_id):
            abort(404, message="Item not found")
        books = [book for book in books if book["id"] != book_id]
        return ''


# 엔드포인트 구현...