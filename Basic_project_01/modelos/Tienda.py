class Tienda:
    _clientes = []
    _libros = []
    _peliculas = []

    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.dinero = 0

