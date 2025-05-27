# Main Program
if __name__ == "__main__":
    my_library = Library(["Python Basics", "C Programming", "JavaScript Guide", "Algorithms 101"])

    while True:
        print("\n====== Library Menu ======")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Return a Book")
        print("4. Add a Book")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            my_library.display_books()
        elif choice == '2':
            book = input("Enter the name of the book to lend: ")
            user = input("Enter your name: ")
            my_library.lend_book(book, user)
        elif choice == '3':
            book = input("Enter the name of the book to return: ")
            my_library.return_book(book)
        elif choice == '4':
            book = input("Enter the name of the book to add: ")
            my_library.add_book(book)
        elif choice == '5':
            print("\nThank you for using the Library System.")
            break
        else:
            print("\nInvalid choice. Please try again.")
