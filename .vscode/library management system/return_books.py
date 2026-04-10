from utils import *

def return_book():
    book_name = input("Enter book name to return:").strip().upper()
    if book_name in issued_books:
        issued_books.remove(book_name)
        books.append(book_name)
        print(f"{book_name} returned successfully.")
    else:
        print(f"{book_name} was not issued from the library.")