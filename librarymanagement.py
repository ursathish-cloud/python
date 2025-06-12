class Library:
    def __init__(self, book_list):
        self.books = book_list
        self.lent_books = {}

    def display_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            if book not in self.lent_books:
                print(f" - {book}")

    def lend_book(self, book, user):
        if book not in self.books:
            print("Book not found in library.")
        elif book in self.lent_books:
            print(f"Book is already lent to {self.lent_books[book]}")
        else:
            self.lent_books[book] = user
            print(f"Book '{book}' lent to {user}")

    def return_book(self, book):
        if book in self.lent_books:
            self.lent_books.pop(book)
            print(f"Book '{book}' returned")
        else:
            print("This book was not borrowed.")

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book}' added to library")

# Main program
def main():
    my_library = Library(["Python Basics", "DSA in C", "HTML and CSS", "Artificial Intelligence"])

    while True:
        print("\nLibrary Menu")
        print("1. Display Books")
        print("2. Lend Book")
        print("3. Return Book")
        print("4. Add Book")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            my_library.display_books()
        elif choice == '2':
            book = input("Enter the book name to lend: ")
            user = input("Enter your name: ")
            my_library.lend_book(book, user)
        elif choice == '3':
            book = input("Enter the book name to return: ")
            my_library.return_book(book)
        elif choice == '4':
            book = input("Enter the name of the book to add: ")
            my_library.add_book(book)
        elif choice == '5':
            print("Exiting Library System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1 to 5.")

if __name__ == "__main__":
    main()
