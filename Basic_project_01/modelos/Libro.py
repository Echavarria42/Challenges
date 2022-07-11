
class Libro:
    _libros = []

    def __init__(self, nombre, autor, num_paginas, editorial, contenido, genero, precio_venta, precio_alquiler, cant_disponible):
        self.nombre = nombre
        self.autor = autor
        self.num_paginas = num_paginas
        self.editorial = editorial
        self.contenido = contenido
        self.genero = genero
        self.prestamos = 0
        self.precio_venta = precio_venta
        self.precio_alquiler = precio_alquiler
        self.cantidad_disponible = cant_disponible
        Libro._libros.append(self)
    
    def prestar(self):
        self.prestamos += 1
        self.cantidad_disponible -= 1
    
    def leer(self):
        pass

    @classmethod
    def get_libros(cls):
        return cls._libros