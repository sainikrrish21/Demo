from utils import books

def show_book():
    if len(books)==0:
        print("No books available.")
    else:
        print("Books available:")
        for book in books:
            print(book)