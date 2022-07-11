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
    c1 = Client(1034234654, "Mateo", "echavarria.0042@gmail.com", 123123123)
    c1.save_client()

    p1 = Movie("Nemo", 2004, 120, 8, "familiar", 50000, 2000, 5)
    p1.save_movie()

    l1 = Book("Poemas", "Mateo Echavarria", "Independiente", "Y nuestras almas vueltas una sola como si nos hubieran forjado con el mismo odio", "poesia", 20000, 2000, 1)
    l1.save_book()