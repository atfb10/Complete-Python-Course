from json import dump

from utils import database

# All caps should indicate a variable that is a constant - never changes value
USER_CHOICE = '''
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit
Your Choice: '''

def menu(menu_options) -> None:
    # Get initial user input
    user_input = input(menu_options)
    while user_input != 'q':
        # Do what the user says to do
        if user_input == 'a':
            name = input('Book Title: ')
            author = input('Author: ')
            add_book(database.books, name, author)
            print('Book Has been Successfully Added!')
        elif user_input == 'l': 
            list_books(database.books)
        elif user_input == 'r': 
            user_input = input('Title of Book to Mark: ')
            mark_book(database.books, user_input)
        elif user_input == 'd': 
            user_input = input('Title of Book to Delete: ')
            delete_book(database.books, user_input)
        elif user_input == 'q':
           print('Goodbye!') 
        else:
            print('Invalid Selection. Try again')
        # Get user input again and again until quit is selected
        user_input = input(menu_options)
    return
        

# Functions to perform action user requests
def add_book(books, name, author) -> None:
    books.append({'name': name, 'author': author, 'read': False}) 
    return

def list_books(books) -> None:
    for i in range(len(books)):
        print(books[i]['name'])
    return

def mark_book(books, book_title) -> None:
    for book in books:
        if book['name']== book_title:
            book['read'] = True
            print('Book has been marked')
            print(f"{book['name']} has been read? {book['read']}")
            return
    print('Book entered is not in the list')
    return
    
def delete_book(books, book_title) -> None:
    for i in range(len(books)):
        if books[i]['name'] == book_title:
            del books[i]
            print('Book deleted')
            return
    print('Book entered is not in the list')     
    return

def write_books_to_JSON(books) -> None:
    with open('books-json.txt', 'w') as write_file:
        dump(books, write_file)
    return

def write_books_to_CSV(books) -> None:
    with open('books-csv.txt', 'w') as write_file:
        for i in range(len(books)):
            if i + 1 < len(books):
                name = books[i]['name']
                author = books[i]['author']
                read = books[i]['read']
                line = f"{name},{author},{read}\n"
                write_file.write(line)
            else:
                name = books[i]['name']
                author = books[i]['author']
                read = books[i]['read']
                line = f"{name},{author},{read}"
                write_file.write(line)

menu(USER_CHOICE)
write_books_to_JSON(database.books)
write_books_to_CSV(database.books)