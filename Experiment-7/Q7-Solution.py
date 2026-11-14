# Experiment 7: Library Management System

class LibraryItem:
    def __init__(self, item_id, title):
        self.item_id = item_id
        self.title = title
        self.issued = False

    def display(self):
        print("ID:", self.item_id)
        print("Title:", self.title)
        print("Status:", "Issued" if self.issued else "Available")

    def issue(self):
        if not self.issued:
            self.issued = True
            print("Item issued successfully.")
        else:
            print("Item is already issued.")

    def return_item(self):
        if self.issued:
            self.issued = False
            print("Item returned successfully.")
        else:
            print("Item was not issued.")


class Book(LibraryItem):
    def __init__(self, item_id, title, author):
        super().__init__(item_id, title)
        self.author = author

    def display(self):
        print("\nBook Details")
        super().display()
        print("Author:", self.author)


class Magazine(LibraryItem):
    def __init__(self, item_id, title, issue_number):
        super().__init__(item_id, title)
        self.issue_number = issue_number

    def display(self):
        print("\nMagazine Details")
        super().display()
        print("Issue Number:", self.issue_number)


class Journal(LibraryItem):
    def __init__(self, item_id, title, research_area):
        super().__init__(item_id, title)
        self.research_area = research_area

    def display(self):
        print("\nJournal Details")
        super().display()
        print("Research Area:", self.research_area)


library = []

while True:
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. Add Magazine")
    print("3. Add Journal")
    print("4. Display All Items")
    print("5. Issue Item")
    print("6. Return Item")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item_id = input("Enter book ID: ")
        title = input("Enter book title: ")
        author = input("Enter author: ")
        library.append(Book(item_id, title, author))
        print("Book added successfully.")

    elif choice == 2:
        item_id = input("Enter magazine ID: ")
        title = input("Enter magazine title: ")
        issue_number = input("Enter issue number: ")
        library.append(Magazine(item_id, title, issue_number))
        print("Magazine added successfully.")

    elif choice == 3:
        item_id = input("Enter journal ID: ")
        title = input("Enter journal title: ")
        area = input("Enter research area: ")
        library.append(Journal(item_id, title, area))
        print("Journal added successfully.")

    elif choice == 4:
        if not library:
            print("Library is empty.")
        else:
            for item in library:
                item.display()

    elif choice == 5:
        item_id = input("Enter item ID to issue: ")

        for item in library:
            if item.item_id == item_id:
                item.issue()
                break
        else:
            print("Item not found.")

    elif choice == 6:
        item_id = input("Enter item ID to return: ")

        for item in library:
            if item.item_id == item_id:
                item.return_item()
                break
        else:
            print("Item not found.")

    elif choice == 7:
        print("Exiting Library Management System.")
        break

    else:
        print("Invalid choice.")