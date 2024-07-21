#!/usr/bin/env python3
#python class for ALX backend program

class Book:
    """A simple class for learning purposes"""
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        #"(title) by (author), published in (year)"
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        #f"Book('{self.title}', '{self.author}', {self.year})"
        return f"Book('{self.title}', '{self.author}' , {self.year})"

    def __del__(self):
        #"Deleting (title of the book)"
        print(f"Deleting {self.title}")

