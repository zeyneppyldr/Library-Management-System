class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        books = self.file.readlines()
        if not books:
            print("There are no books to list in the library")
        else:
            print("Books:")
            for book in books:
                title, author, release_year, num_pages = book.strip().split(',')
                print(f"Title: {title}, Author: {author}, Release Year: {release_year}, Pages: {num_pages}")

    def add_book(self):
        title = input("Enter the book title: ")
        author = input("Enter the author name: ")
        release_year = input("Enter the first release year: ")
        num_pages = input("Enter the number of pages: ")
    
        book_info = f"{title},{author},{release_year},{num_pages}\n"

        self.file.seek(0)
        if book_info in self.file.read():
            print("This book is already on the list.")
        else:
            self.file.write(book_info)
            print(f"Book '{title}' added successfully.")
             
    def remove_book(self):
        title = input("Enter the book title: ")
        author = input("Enter the author name: ")
        release_year = input("Enter the first release year: ")
        num_pages = input("Enter the number of pages: ")
    
        book_info = f"{title},{author},{release_year},{num_pages}\n"

        self.file.seek(0)
        books = self.file.readlines()
        for i, book in enumerate(books):
            if title in book:
                del books[i]
                break
            else:
                print(f"Book '{title}' not found.")
                return

        self.file.seek(0)
        self.file.truncate()
        self.file.writelines(books)
        print(f"Book '{title}' removed successfully.")
        
    def find_book(self):
        search_title = input("Enter title of the book to search: ")
        search_author = input("Enter author of the book to search: ")
        self.file.seek(0)
        books = self.file.readlines()
        found = False
        for book in books:
            book_info = book.strip().split(",")
            if search_title.lower() in book_info[0].lower() and search_author.lower() in book_info[1].lower():
                found = True
                print(f"Book found: {book_info}")
        if not found:
            print(f"Book '{search_title}' by '{search_author}' not found in the library.")


lib = Library()

while True:
    print("*** MENU***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Find Book")
    print("Q) Quit")

    choice = input("Enter your choice (1/2/3/4/Q): ")

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    elif choice == "4":
        lib.find_book()
    elif choice =="Q" :
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")