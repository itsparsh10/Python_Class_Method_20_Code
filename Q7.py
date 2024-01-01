#Implement a class inheritance as following:
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def add_book(self, book_type):
        print(f"{book_type.title} by {book_type.author} added to the store!")


class Fiction(Book):
    def __init__(self, title, author, genre):
        super().__init__(title, author)
        self.genre = genre

    def add_book(self, book_type):
        print(f"{book_type.title} by {book_type.author} in the {self.genre} genre added to the store!")


class NonFiction(Book):
    def __init__(self, title, author, subject):
        super().__init__(title, author)
        self.subject = subject

    def add_book(self, book_type):
        print(f"{book_type.title} by {book_type.author} on the subject of {self.subject} added to the store!")


class Mystery(Book):
    def __init__(self, title, author, detective):
        super().__init__(title, author)
        self.detective = detective

    def add_book(self, book_type):
        print(f"{book_type.title} by {book_type.author} featuring Detective {self.detective} added to the store!")


def main():
    print("----WELCOME TO THE BOOKSTORE (Admin Side)----")

    while True:
        print("\n\n1)Regular Books")
        print("2)Fiction Books")
        print("3)Non-Fiction Books")
        print("4)Mystery Books")
        print("5.Exit")
        choice = int(input("\nWhat do you want to add: "))

        if choice == 1:
            title = input("\nEnter title of the book: ")
            author = input("Enter author: ")
            book = Book(title, author)
            book.add_book(book)

        elif choice == 2:
            print("\nWelcome to the Fiction section!\n")
            title = input("Enter title of the fiction book: ")
            author = input("Enter author of the fiction book: ")
            genre = input("Enter the genre: ")
            fiction_book = Fiction(title, author, genre)
            fiction_book.add_book(fiction_book)

        elif choice == 3:
            print("\nWelcome to Non-Fiction Books Section!\n")
            title = input("Enter title of the non-fiction book: ")
            author = input("Enter author of the non-fiction book: ")
            subject = input("Enter the subject: ")
            non_fiction_book = NonFiction(title, author, subject)
            non_fiction_book.add_book(non_fiction_book)

        elif choice == 4:
            print("\nWelcome to the Mystery Books Section\n")
            title = input("Enter title of the mystery book: ")
            author = input("Enter author of the mystery book: ")
            detective = input("Enter the detective featured: ")
            mystery_book = Mystery(title, author, detective)
            mystery_book.add_book(mystery_book)

        elif choice == 5:
            print("Exiting...")
            break
        
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
