from app import books

books_generator=(x for x in books)

USER_CHOICE= '''Enter one of the following

-'b' to get 5-star books
-'n' to get next book available
-'c' to get the cheapest books
-'q' to quit the application
'''


def print_best_books():
    best_books=sorted(books, key=lambda x: x.rating*(-1))[:10]
    for b in best_books:
       print(b)


def print_cheapest_books():
    cheapest_books=sorted(books, key=lambda x: x.price)[:10]
    for b in cheapest_books:
       print(b)


def get_next_book():
    print(next(books_generator))


user_choices = {
        'b': print_best_books,
        'c': print_cheapest_books,
        'n': get_next_book
    }

def menu():
    user_input=input(USER_CHOICE)
    while user_input!= 'q':
        if user_input in ('b','c','n'):
            user_choices[user_input]()
        else:
            print('Please choose a valid command')
        user_input = input(USER_CHOICE)

menu()

