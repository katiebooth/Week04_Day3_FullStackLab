from models.author import Author
from models.book import Book

from repositories import author_repository 
from repositories import book_repository 

#delete the book (child) first, otherwise the parent (author) will break
book_repository.delete_all()
author_repository.delete_all()

#define some authors before the books as books need an instance of author
author1 = Author("J.K. Rowling")
author_repository.save(author1)
author2 = Author("George R.R. Martin")
author_repository.save(author2)
author3 = Author("Roald Dahl")
author_repository.save(author3)

#return the author ids to be put into books
print(author_repository.select_all())

book1 = Book("HP and the Chamber of Secrets", "Fantasy", author1)
book_repository.save(book1)
book2 = Book("HP and the Prisoner of Azkaban", "Fantasy", author1)
book_repository.save(book2)
book3 = Book("Feast for Crows", "Fantasy", author2)
book_repository.save(book3)
book4 = Book("Dance of the Dragons", "Fantasy", author2)
book_repository.save(book4)
book5 = Book("Matilda", "Childrens", author3)
book_repository.save(book5)
book6 = Book("Charlie and the Chocolate Factory", "Childrens", author3)
book_repository.save(book6)
print(book_repository.select_all())

#HOW TO UPDATE IN THE BACK END WITH A ONE-TO-MANY?
# book_to_update = Book("Update", "Update", author1, book1.id)
# book_repository.update(book_to_update)

print(book_repository.select_all())
