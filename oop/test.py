#!/usr/bin/env python3
#python script related to the ALX backend program

class Book:
    """A simple class for learning purposes"""
    def __init__(self, title, author):
        self.title = title
        self.author = author

class EBook(Book):
    """A simple derived class for learning purposes"""
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

class PrintBook(Book):
    """A simple derived class for learning purposes"""
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

class Library:
    """A simple class that serves as a composition"""

        self.book = book #Here I perform a class composition


    def add_book(self, book):
        self.book.add(
        self.

