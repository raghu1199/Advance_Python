from .database_connection_contextManager import DatabaseConnection
import sqlite3


def create_book_table():
    with DatabaseConnection("data.db") as connection:
        cursor = connection.cursor()
        cursor.execute("create table if not exists books(name text primary key,author text,read integer)")


def add_book(name, author):
    with DatabaseConnection("data.db") as connection:
        cursor = connection.cursor()
        cursor.execute("insert into books values(?,?,0)", (name, author))


def get_all_books():
    con = sqlite3.connect("data.db")
    cursor = con.cursor()
    cursor.execute("select * from books")
    books = [
        {'name': row[0], "author": row[1], "read": row[2]}
        for row in cursor.fetchall()
    ]
    con.close()
    return books


def mark_book_as_read(name):
    con = sqlite3.connect("data.db")
    cursor = con.cursor()
    cursor.execute("update books set read=1 where name=?",
                   (name,))  # onlytuplsshould be used single elemnt tuple (name,)
    con.commit()
    con.close()


def delete_book(name):
    con = sqlite3.connect("data.db")
    cursor = con.cursor()
    cursor.execute("delete from books where name=?", (name,))
    con.commit()
    con.close()
