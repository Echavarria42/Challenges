from unittest.mock import Mock
from models.Movie import Movie
from models.Book import Book
from models.Client import Client


def menu():
    aux = -1
    while aux != 5:
        aux = int(input("""
[1] Prestar Libro
[2] Comprar Libro
[3] Prestar Pelicula
[4] Comprar Pelicula
[5] Salir
"""))

        if aux == 1:
            pass

if __name__ == "__main__":
    c1 = Client(1034234654, "User1", "example1@example.com", 123123123)
    c2 = Client(1036534654, "User2", "example2@example.com", 123423123)
    c3 = Client(1036534654, "User2", "example2@example.com", 123423123)

    p1 = Movie("Nemo", 2004, 120, 8, "familiar", 50000, 2000, 5)
    p2 = Movie("Nemo", 2004, 120, 8, "familiar", 50000, 2000, 5)
    p3 = Movie("Paladins", 2032, 240, 16, "accion-futurista", 80000, 3500, 2) 

    l1 = Book("Libro1", "Author1", "Independiente", "Contenido2", "None", 20000, 2000, 3)
    l2 = Book("Libro2", "Author2", "Independiente", "Contenido1", "None", 35000, 7000, 4)
    l3 = Book("Libro2", "Author2", "Independiente", "Contenido1", "None", 35000, 7000, 4)

    print(Book.get_books())
    print(Client.get_clients())
    print(Movie.get_movies())
