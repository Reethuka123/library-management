import os
import sys
import time

DATA_FILE = "library_books.txt"

# Each book is stored as a dictionary
books = []

# Load books from file
def load_books():
    if not os.path.exists(DATA_FILE):
        return
    with open(DATA_FILE, 'r') as f:
        for line in f:
            title, author, status = line.strip().split('|')
            books.append({'title': title, 'author': author, 'status': status})

# Save books to file
def save_books():
    with open(DATA_FILE, 'w') as f:
        for book in books:
            f.write(f"{book['title']}|{book['author']}|{book['status']}\n")

def add_book():
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    books.append({'title': title, 'author': author, 'status': 'Available'})
    print(f"✅ Book '{title}' added successfully!\n")

def view_books():
    if not books:
        print("📚 No books in the library yet.\n")
        return
    print("\n--- Library Books ---")
    for i, book in enumerate(books, 1):
        print(f"{i}. {book['title']} by {book['author']} [{book['status']}]")
    print()

def search_books():
    keyword = input("🔍 Enter title keyword to search: ").lower()
    found = [b for b in books if keyword in b['title'].lower()]
    if found:
        print("\n🔎 Search Results:")
        for book in found:
            print(f"{book['title']} by {book['author']} [{book['status']}]")
    else:
        print("🚫 No books found with that title.\n")
    print()

def borrow_book():
    title = input("Enter the title to borrow: ").strip()
    for book in books:
        if book['title'].lower() == title.lower():
            if book['status'] == 'Available':
                book['status'] = 'Borrowed'
                print(f"📕 You borrowed '{book['title']}'\n")
                return
            else:
                print("❌ This book is already borrowed.\n")
                return
    print("🚫 Book not found.\n")

def return_book():
    title = input("Enter the title to return: ").strip()
    for book in books:
        if book['title'].lower() == title.lower():
            if book['status'] == 'Borrowed':
                book['status'] = 'Available'
                print(f"📗 You returned '{book['title']}'\n")
                return
            else:
                print("❌ This book was not borrowed.\n")
                return
    print("🚫 Book not found.\n")

def main_menu():
    while True:
        print("\n📘 LIBRARY MANAGEMENT SYSTEM")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Book by Title")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Exit")
        choice = input("Choose an option (1-6): ").strip()

        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            search_books()
        elif choice == '4':
            borrow_book()
        elif choice == '5':
            return_book()
        elif choice == '6':
            print("📥 Saving and exiting...")
            save_books()
            time.sleep(1)
            print("Goodbye")
            sys.exit()
        else:
            print("⚠️ Invalid choice. Try again.\n")

# Load books and run the menu
load_books()
main_menu()
