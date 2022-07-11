
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
    
    def prestar_libro(self, libro : Libro):
        libro.prestar()
        self.libros_prestados.append(libro)
    
    def prestar_pelicula(self, pelicula : Pelicula):
        pelicula.prestar()
        self.libros_prestados.append(pelicula)
    

    def guardar_cliente(self):
        from main import guardar_archivo
        import main
        main.ruta = "archivos/clientes.txt"

        @guardar_archivo
        def guardar():
            return f"{self.nombre},{self.cc},{self.email},{self.celular},{self.libros_prestados},{self.peliculas_prestadas}"

        return guardar()

    @classmethod
    def get_clientes(cls):
        return cls._clientes