from decorators import save_file, only

class Book:
    _books = []

    def __init__(self, name, author, publisher, content, genre, sale_price, rental_price, available_quantity):
        self.name = name
        self.author = author
        self.publisher = publisher
        self.content = content
        self.genre = genre
        self.loans = 0
        self.sale_price = sale_price
        self.rental_price = rental_price
        self.available_quantity = available_quantity

        @only
        def comprobar(self):
            Book._books.append(self)               
        comprobar(self)
    
    def rent(self):
        self.loans += 1
        self.available_quantity -= 1
    
    def leer(self):
        pass

    @save_file
    def save(self):
        return f'{self.name}\n{self.author}\n{self.publisher} - {self.genre}\n{self.content}'

    @classmethod
    def get_books(cls):
        return cls._books

    def __str__(self) -> str:
        return f"{self.name},{self.author},{self.publisher},{self.content},{self.loans},{self.sale_price},{self.rental_price},{self.available_quantity}"