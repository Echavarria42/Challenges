from modelos.Libro import Libro
from modelos.Pelicula import Pelicula

class Cliente:
    _clientes = []

    def __init__(self, cc, nombre, email, celular):
        self.cc = cc
        self.nombre = nombre
        self.email = email
        self.celular = celular
        self.libros_prestados = []
        self.peliculas_prestadas = []
        Cliente._clientes.append(self)
    
    def prestar_libro(self, libro : Libro):
        libro.prestar()
        self.libros_prestados.append(libro)
    
    def prestar_pelicula(self, pelicula : Pelicula):
        pelicula.prestar()
        self.libros_prestados.append(pelicula)

    @classmethod
    def get_clientes(cls):
        return cls._clientes