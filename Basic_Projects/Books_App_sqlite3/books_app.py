from utils import database
import sqlite3

USER_CHOICE = """
ENTER :
'a' to add new book
'l' to list all books
'd' to delete book
'r' to mark as read
'q' to quit
Your choice:
"""


def menu():
    database.create_book_table()
    usr_input = input(USER_CHOICE)
    while usr_input != 'q':
        if usr_input == 'a':
            prompt_add_book()
        elif usr_input == 'l':
            list_books()
        elif usr_input == 'r':
            prompt_read_book()
        elif usr_input == 'd':
            prompt_delete_book()
        else:
            print("unknown command")
        usr_input = input(USER_CHOICE)


def prompt_add_book():
    name = input("Enter the new book name:")
    author = input("Enter Author name:")

    database.add_book(name, author)


def list_books():
    books = database.get_all_books()
    for book in books:
        read = 'YES' if book['read'] else 'NO'
        print(f"{book['name']} by {book['author']} read:{read}")


def prompt_read_book():
    name = input("Enter the book name you just finished reading")
    database.mark_book_as_read(name)


def prompt_delete_book():
    name = input("Enter the name of book u want to delete")
    database.delete_book(name)


menu()
