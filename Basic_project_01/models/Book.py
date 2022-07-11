
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
        Book._books.append({
            "name" : name,
            "author" : author,
            "publisher" : publisher,
            "content" : content,
            "loans" : self.loans,
            "sale_price" : sale_price,
            "rental_price" : rental_price,
            "available_quantity" : available_quantity
            })
    
    def rent(self):
        self.loans += 1
        self.available_quantity -= 1
    
    def leer(self):
        pass

    def save_book(self):
        from main import save_file
        import main
        main.route = f"files/Books/{self.name}.txt"

        @save_file
        def save():
            return f"""{self.name}
{self.author}
{self.publisher}
{self.genre}
{self.content}"""

        return save()

    @classmethod
    def get_Books(cls):
        return cls._Books