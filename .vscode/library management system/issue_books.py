from utils import books
from utils import issued_books

def issue_book():
    if len(books)==0:
        print("No books available to issue.")
    else:
        book_name = input("Enter book name to issue:").strip().upper()
        if book_name in books:
            books.remove(book_name)
            issued_books.append(book_name)
            print(f"{book_name} issued successfully.")
        else :
            print(f"{book_name} is not available in the library.")