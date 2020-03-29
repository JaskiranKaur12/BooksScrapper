from app import books

def print_best_books():
    best_books=sorted(books, key=lambda x: x.rating*(-1))[:10]
    for b in best_books:
       print(b)


def print_cheapest_books():
    cheapest_books=sorted(books, key=lambda x: x.price)[:10]
    for b in cheapest_books:
       print(b)


print("-----BEST BOOKS-----")
print_best_books()

print("-----CHEAPEST BOOKS-----")
print_cheapest_books()