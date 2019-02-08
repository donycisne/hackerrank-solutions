'''
Task:
  Given a Book class and a Solution class,
  write a MyBook class that does the following:
  - Inherits from Book
  - Has a parameterized constructor taking these 3 parameters:
    1 - string title.
    2 - string author.
    3 - int price.
  - Implements the Book class' abstract display() method so it prints these 3 lines:
    1 - Title:, a space, and then the current instance's title.
    2 - Author:, a space, and then the current instance's author.
    3 - Price:, a space, and then the current instance's price.
'''

# Solution
from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
  def __init__(self,title,author):
    self.title=title
    self.author=author
  @abstractmethod
  def display(self):
    pass

#Write MyBook class
class MyBook(Book):
  price = 0
  def __init__(self, title, author, price):
    Book.__init__(self,title,author)
    self.price = price

  def display(self):
    print('➡ Title:', title)
    print('➡ Author:', author)
    print('➡ Price:', str(price))

title=input('Enter a title: ')
author=input('Enter an author: ')
price=int(input('Enter a price: '))
new_novel=MyBook(title,author,price)
new_novel.display()
