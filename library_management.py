"""
Program to create a library using class
and showing how to print all books, add a book 
and get the number of books using different methods.
"""
class Library:
    def __init__(self):
        self.books = ["Fluent Python: Clear, Concise, and Effective Programming",
                "Think Python: An Introduction to Software Design",
                "Python All-in-One For Dummies"]
        print("Welcome to the Library. Select one option:\n1.(Show books)\n2.(no. of books).\n3.(Add book)")
    def showbooks(self):
        print("List of books:")
        for i in self.books:
            print(i) 
    def book_number(self):
        print(f"There are {len(self.books)} books in the library.")
    def add_book(self):
        book = input("Enter book name: ")
        self.books.append(book)
        print("Book added")

library = Library()
while(True):
    option = int(input())
    if(option==1):
        library.showbooks()
    elif(option==2):
        library.book_number()
    elif(option==3):
        library.add_book()
    else:
        break