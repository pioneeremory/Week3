
class LibraryUser():

    number_of_users = 0

    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.has_book = False
        self.borrowed_book = None
        LibraryUser.number_of_users += 1

    def borrow_book(self, book):
        self.book = book

        if self.has_book:
            print('You cannot checkout more than one book')
        else: 
            self.has_book == True
            print('You checked out the book')
            self.borrowed_book = book
            book_title = book.title
            print(f'You have checked out {book_title}')

class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author

@classmethod
def create_book(cls, new_title, new_author):

    return cls(new_title, new_author)

@classmethod
def get_user_count(cls):
    return cls.number_of_users

user_book = create_book("test", "test")
print(create_book(user_book))

class Librarian(LibraryUser):
    def __init__(self, user_name, email)
        super().__init__(user_name, email)

#class method to create book
testbook = Book.create_book("test", "test")

user_logan = LibraryUser("Logan", "email@somewhere.com")
user_logan.borrow_book(testbook)