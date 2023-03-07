from app import books

USER_CHOICE = '''
- 'b' to look at 5 star books
- 'c' to look at cheapest books
- 'n' to get the next available book on the page
- 'q' to quit
Enter Choice: '''

def menu(books):
    generated_books = (book for book in books)
    user_choice = input(USER_CHOICE)
    while user_choice != 'q':
        if user_choice == 'b':
            print_ten_best_books()
        elif user_choice == 'c':
            print_ten_cheapest_books()
        elif user_choice == 'n':
            get_next_book_generator(generated_books)
        else: print('Please make valid selection')
        user_choice = input(USER_CHOICE)


def get_next_book_generator(generated_books):
    new_book = next(generated_books)
    print(new_book)
    return

def get_next_book_indexing(books, index) -> None:
    new_book = books[index]
    print(new_book)
    return

def print_ten_best_books() -> None:
    '''
    for books, sort by the rating
    * -1 makes the list descending
    for descending it would just be: book.rating
    '''
    best_books = sorted(books, key=lambda book: book.rating * -1)[:10]
    for book in best_books:
        print(book)
    return

def print_ten_cheapest_books() -> None:
    cheapest_books = sorted(books, key=lambda book: book.price)[:10]
    for b in cheapest_books:
        print(f'${b.price} - {b.title}')
    return

def print_ten_best_value_books() -> None:
    '''
    returns best books by both price and rating.
    to do this, return a tuple in the lambda function
    '''
    value_books = sorted(books, key=lambda book: ((book.rating * -1), book.price))[:10]
    for book in value_books:
        print(f'{book.title} is ${book.price}. It has {book.rating} stars!')
    return

menu(books)