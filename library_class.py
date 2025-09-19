class Book: #create the Book class
    def __init__(self, book_id, title, author): #giving it properties
        self.book_id = book_id 
        self.title = title 
        self.author = author 
        self.is_loaned = False #Boolean variable
#create the book class with attirbutes toto identify the borrower
class Borrower:
    def __init__(self, borrower_id, name):
        self.borrower_id = borrower_id
        self.name = name
#creates teh lan class and links the book with borrower
class Loan:
    def __init__(self, book, borrower):
        self.book = book
        self.borrower = borrower

class BookManager:
    def __init__(self):
        self.books = {}
#stores books with id as the keys

    def add_book(self, book_id, title, author):
        if book_id in self.books:
            raise ValueError("Book ID already exists.")
        self.books[book_id] = Book(book_id, title, author)

    def remove_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
        else:
            raise ValueError("Book ID not found.")

    def search_book(self, book_id):
        return self.books.get(book_id, None)

class BorrowerManager:
    def __init__(self):
        self.borrowers = {} #stores borrowers id

    def add_borrower(self, borrower_id, name):
        if borrower_id in self.borrowers:
            raise ValueError("Borrower ID already exists.")
        self.borrowers[borrower_id] = Borrower(borrower_id, name)

    def remove_borrower(self, borrower_id):
        if borrower_id in self.borrowers:
            del self.borrowers[borrower_id]
        else:
            raise ValueError("Borrower ID not found.")

    def search_borrower(self, borrower_id):
        return self.borrowers.get(borrower_id, None)
#takes care of the creation and return of loans between  books and borrower
class LoanManager:
    def __init__(self):
        self.loans = []#lists the present loans

    def create_loan(self, book, borrower):
        if book.is_loaned:
            raise ValueError("Book is already loaned.")
        loan = Loan(book, borrower)
        self.loans.append(loan)
        book.is_loaned = True#marks book as loaned

    def return_loan(self, book):
        for loan in self.loans:
            if loan.book.book_id == book.book_id:
                self.loans.remove(loan)
                book.is_loaned = False #marks books as returned
                break