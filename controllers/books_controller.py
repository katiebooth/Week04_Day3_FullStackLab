from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import book_repository
from repositories import author_repository
from models.book import Book

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/books", methods = ['GET'])
def books():
    books_list = book_repository.select_all()
    return render_template("books/index.html", all_books = books_list)

@books_blueprint.route("/books/new", methods = ['GET'])
def new_book():
    authors_list = author_repository.select_all()
    return render_template("books/new.html", all_authors = authors_list)

@books_blueprint.route("/books", methods = ["POST"])
def create_book():
    title = request.form['title']
    genre = request.form['genre']
    author_id = request.form['author_id']
    author = author_repository.select_id(author_id)
    book = Book(title, genre, author)
    book_repository.save(book)
    return redirect('/books')

@books_blueprint.route("/books/delete/<id>", methods = ['POST'])
def delete_book(id):
    book_repository.delete(id)
    return redirect("/books")

@books_blueprint.route("/books/<id>", methods = ['GET'])
def show_book(id):
    book_to_show = book_repository.select_id(id)
    return render_template("books/show.html", book = book_to_show)

@books_blueprint.route("/books/<id>/update", methods=['GET'])
def edit_form(id):
    book_object = book_repository.select_id(id)
    authors_to_show = author_repository.select_all()
    return render_template("/books/edit.html", book=book_object, all_authors = authors_to_show)

@books_blueprint.route("/books/<id>", methods = ['POST'])
def update_book(id):
    title = request.form['title']
    genre = request.form['genre']
    author_id = request.form['author_id']
    author = author_repository.select_id(author_id)
    book = Book(title, genre, author, id)
    book_repository.update(book)
    return redirect("/books")