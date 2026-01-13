# Exercise from Boot.dev OOP lessons
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        wanted_books = []
        for b in self.books:
            if b.title != book.title or b.author != book.author:
                wanted_books.append(b)

        self.books = wanted_books

    def search_books(self, search_string):
        search_list = []
        lowered_search_string = search_string.lower()
        
        for book in self.books:
            lowered_author = book.author.lower()
            lowered_title = book.title.lower()
            
            if lowered_search_string in lowered_author or lowered_search_string in lowered_title:
                search_list.append(book)

        return search_list
