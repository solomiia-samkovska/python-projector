class Book:
    def __init__(self, title, author, category):
        self.title = title
        self.author = author
        self.category = category

class Shelf:
    def __init__(self, category):
        self.category = category
        self.__books = []

    def addBook(self, book: Book):
        self.__books.append(book)
    
    def sortBooks(self):
        self.__books.sort(key = lambda x: x.title)
    
    def listAllBooks(self):
        print("Category: ", self.category)
        for book in self.__books:
            print(book.title, ' ', book.author)

class DigitalCatalog:
    def __init__(self) -> None:
        self.shelves = []

    def addBooks(self, books: set[Book]):
        for book in books:
            shelf = self.getShelfByCategory(book.category)
            shelf.addBook(book)
        
    def getShelfByCategory(self, category: str) -> Shelf:
        for shelf in self.shelves:
            if shelf.category == category:
                return shelf
        
        shelf = Shelf(category)
        self.shelves.append(shelf)
        return shelf
        
    def organiseBooks(self):
        for shelf in self.shelves:
            shelf.sortBooks()

    def printAllBooks(self):
        for shelf in self.shelves:
            shelf.listAllBooks()
            
def generateBooks():
    return {
        Book("The Great Gatsby", "F. Scott Fitzgerald", "Classic"),
        Book("To Kill a Mockingbird", "Harper Lee", "Classic"),
        Book("ATo Kill a Mockingbird", "Harper Lee", "Classic"),
        Book("DTo Kill a Mockingbird", "Harper Lee", "Classic"),
        Book("CTo Kill a Mockingbird", "Harper Lee", "Classic"),
        Book("BTo Kill a Mockingbird", "Harper Lee", "Classic"),
        Book("1984", "George Orwell", "Dystopian"),
        Book("Brave New World", "Aldous Huxley", "Dystopian")
    }


books = generateBooks()

catalog = DigitalCatalog()
catalog.addBooks(books)
catalog.organiseBooks()
catalog.printAllBooks()

    