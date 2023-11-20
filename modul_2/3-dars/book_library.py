class Book:
    def __init__(self, title: str, author: str, is_borrowed=False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def borrow(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return f"Now, {self.title} is available to borrow!"
        else:
            return f"Now, {self.title} isn't available to borrow!"

    def return_book(self):
        if not self.is_borrowed:
            return f"Now, {self.title} has allready returned!"
        else:
            self.is_borrowed = True
            return f"Thanks, you return book called {self.title}!"


class Library:
    def __init__(self, name: str):
        self._name = name
        self._books: list[Book] = []

    def add_book(self, book: Book):
        book.is_borrowed = True
        self._books.append(book)

    def list_books(self):
        for book in self._books:
            print(f"Title: {book.get_title()}\n"
                  f"Author: {book.get_author()}\n"
                  f"Available: {book.is_borrowed}\n")


book1 = Book("Harry Potter", "J.K.Rowling")
book2 = Book("Moby-Dick", "Herman Melville")
book3 = Book("Anna Karenina", "Leo Tolstoy")

library = Library("Milliy")
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.list_books()
