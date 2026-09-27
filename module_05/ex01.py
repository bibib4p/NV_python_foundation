# Find it - Finding a book in the collection

books = [
    "The Brothers Karamazov",
    "Crime and Punishment",
    "White Nights",
    "Notes from Underground",
    "The Idiot",
    "The Gambler",
    "Demons",
    "A Raw Youth",
    "Poor Folk",
    "Notes from the House of the Dead",
]


def main():
    book = input("Search for a book: ").strip().title()
    if search_book(book):
        print(f"{book} is in the collection")
    else:
        print(f"Sorry! {book} is not in the collection")


def search_book(name):
    if name in books:
        return True
    else:
        return False


# Loop thru list items
# def search_book(name):
#     for book in books:
#         if book == name:
#             return True
#     return False

# Loop thru index numbers
# def search_book(name):
#     for i in range(len(books)):
#         if books[i] == name:
#             return True
#     return False

# while loop thru list items
# def search_book(name):
#     i = 0
#     while i < len(books):
#         if books[i] == name:
#             return True
#         i += 1
#     return False


main()
