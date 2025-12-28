from flask import Blueprint, request, jsonify
from extensions import db
from models.book import Book

book_bp = Blueprint("books", __name__)

@book_bp.route("/", methods=["POST"])
def create_book():
    data = request.get_json()

    book = Book(
        title=data["title"],
        author=data["author"],
        isbn=data.get("isbn"),
        published_year=data.get("published_year"),
        quantity=data.get("quantity", 1)
    )

    db.session.add(book)
    db.session.commit()

    return jsonify(book.to_dict()), 201


@book_bp.route("/", methods=["GET"])
def get_books():
    books = Book.query.all()
    return jsonify([b.to_dict() for b in books])


@book_bp.route("/<int:id>", methods=["GET"])
def get_book(id):
    book = Book.query.get_or_404(id)
    return jsonify(book.to_dict())


@book_bp.route("/<int:id>", methods=["PUT"])
def update_book(id):
    book = Book.query.get_or_404(id)
    data = request.get_json()

    book.title = data.get("title", book.title)
    book.author = data.get("author", book.author)
    book.isbn = data.get("isbn", book.isbn)
    book.published_year = data.get("published_year", book.published_year)
    book.quantity = data.get("quantity", book.quantity)

    db.session.commit()
    return jsonify(book.to_dict())


@book_bp.route("/<int:id>", methods=["DELETE"])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": "Book deleted"})
