'''
Description: Concerned with storing & receiving books from a list
Author: Adam Forestier
Date: Feb 28, 2023
'''
import sqlite3 as sql
from .database_connection import DatabaseConnection

HOST = 'data.db'

# Steps: 1. Connect 2. Cursor 3. Perform Query w/ cursor 4. Commit connection *IF* writing to DB 5. Close connection
def create_book_table() -> None:
    # Connect using context manager
    with DatabaseConnection(HOST) as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS BOOKS(name text primary key, author text, read integer)')
    return

def insert_book(name, author) -> None:
    # Connect by opening and closing connection manually
    connection = sql.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('INSERT INTO BOOKS VALUES(?, ?, 0)', (name, author))

    connection.commit()
    connection.close()
    return

def list_all_books() -> None:
    with DatabaseConnection(HOST) as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * from BOOKS')

        # How to read from the database. SELECT * FROM BOOKS returns list of tuples -> [(name, author, read), (name, author, read)]
        book_list = cursor.fetchall()

        # Example of how to turn fetchall into a list of dictionaries
        dict_book_list = [{'name':row[0], 'author':row[1], 'read':row[2]} for row in cursor.fetchall()]

    for i in range(len(book_list)):
        print(f'{book_list[i][0]} by {book_list[i][1]}. Read: {book_list[i][2]}')
    return

def mark_read(book_name) -> None:
    with DatabaseConnection(HOST) as connection:
        cursor = connection.cursor()
        cursor.execute('UPDATE BOOKS SET read=1 WHERE name=?', (book_name,))
    return

def delete_book(book_name) -> None:
    with DatabaseConnection(HOST) as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM BOOKS WHERE name=?', (book_name,))
    return