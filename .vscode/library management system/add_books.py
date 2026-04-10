from utils import books

def add_book():
    book_name = input("Enter book name to add:").strip().upper()
    books.append(book_name)
    print(f"{book_name} added successfully.")