# Author class
class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author is self]

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        return Contract(author=self, book=book, date=date, royalties=royalties)

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())

    def __repr__(self):
        return f'Author(name={self.name})'


# Book class
class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book is self]
    
    def authors(self):
        return [contract.author for contract in self.contracts()]

    def __repr__(self):
        return f'Book(title={self.title})'


# Contract class
class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if isinstance(new_author, Author):
            self._author = new_author
        else:
            raise Exception('Contract.author must be an Author instance')

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, new_book):
        if isinstance(new_book, Book):
            self._book = new_book
        else:
            raise Exception('Contract.book must be a Book instance')

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, new_date):
        if isinstance(new_date, str):
            self._date = new_date
        else:
            raise Exception('Contract.date must be a string')

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, new_royalties):
        if isinstance(new_royalties, int) and new_royalties >= 0:
            self._royalties = new_royalties
        else:
            raise Exception('Contract.royalties must be a non-negative integer')

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]

    def __repr__(self):
        return f'Contract(author={self.author}, book={self.book}, date={self.date}, royalties={self.royalties})'


# Instantiate the classes
b1 = Book(title='Tale of Two Cities')
a1 = Author(name='Charles Dickens')
c1 = Contract(author=a1, book=b1, date='2025-01-09', royalties=1000)

# Test signing a contract
a1.sign_contract(b1, '2025-01-10', 2000)
print(a1.contracts())
print(a1.books())
print(a1.total_royalties())
print(Contract.contracts_by_date('2025-01-09'))
