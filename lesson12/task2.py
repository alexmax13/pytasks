# Task 2

# Write a class structure that implements a library. Classes:
# 1) Library - name, books = [], authors = []
# 2) Book - name, year, author (author must be an instance of Author class)
# 3) Author - name, country, birthday, books = []

# Library class
# Methods:
# - new_book(name: str, year: int, author: Author) - returns an instance of Book class
#   and adds the book to the books list for the current library.
# - group_by_author(author: Author) - returns a list of all books grouped by the specified author
# - group_by_year(year: int) - returns a list of all the books grouped by the specified year

# All 3 classes must have a readable __repr__ and __str__ methods.
# Also, the book class should have a class variable which holds the amount of all existing books


class Library:

    def __init__(self):
        self.books = []

    def new_book(self, title, year, author):
        self.books.append(Book(title, year, author))
        Book.amount += 1

    def group_by_author(self, author):
        buffer = ''
        for book in self.books:
            if book.author == author:
                buffer += str(book)
                buffer += '\n'
        return buffer

    def group_by_year(self, year):
        buffer = ''
        for book in self.books:
            if book.year == year:
                buffer += str(book)
                buffer += '\n'
        return buffer

    def __repr__(self):
        return self.books

    def __str__(self):
        buffer = ''
        for book in self.books:
            buffer += str(book)
            buffer += '\n'
        return buffer


class Book:
    amount = 0

    def __init__(self, title, year, author):
        self.title = title
        self.year = year
        self.author = author

    def __repr__(self):
        return f'{self.title} - {self.year} рік, ({self.author})'

    def __str__(self):
        return f'{self.title} - {self.year} рік, ({self.author})'


class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


author_remark = Author('Еріх Марія Ремарк', 'Німеччина', 1898)
author_sartr = Author('Жан Поль Сартр', 'Франція', 1890)


library = Library()
library.new_book('Тошнота', 1938, author_sartr)
library.new_book('Слова', 1964, author_sartr)
library.new_book('Мухи', 1943, author_sartr)


library.new_book('Три товариші', 1936, author_remark)
library.new_book('Возвращение', 1931, author_remark)
library.new_book('Триумфальная арка', 1945, author_remark)
library.new_book('Искра жизни', 1931, author_remark)

print(library.group_by_author(author_sartr), end='\n' * 2)
print(library.group_by_author(author_remark), end='\n' * 2)

print(library.group_by_year(1931), end='\n' * 2)

print(library)

print(f'{Book.amount} books in library.')
