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
            database.insert_book(name, author)
            print('Book Has been Successfully Added!')
        elif user_input == 'l': 
            database.list_all_books()
        elif user_input == 'r': 
            user_input = input('Title of Book to Mark: ')
            database.mark_read(user_input)
        elif user_input == 'd': 
            user_input = input('Title of Book to Delete: ')
            database.delete_book(user_input)
        else:
            print('Invalid Selection. Try again')
        # Get user input again and again until quit is selected
        user_input = input(menu_options)
    return

database.create_book_table()
menu(USER_CHOICE)