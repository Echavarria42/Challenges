class Pelicula:
    _peliculas = []

    def __init__(self, nombre, anho, duracion_min, edad_permitida, genero, precio_venta, precio_alquiler, cant_disponible):
        self.nombre = nombre
        self.anho = anho
        self.duracion_min = duracion_min
        self.edad_permitida = edad_permitida
        self.genero = genero
        self.prestamos = 0
        self.precio_venta = precio_venta
        self.precio_alquiler = precio_alquiler
        self.cantidad_disponible = cant_disponible
        Pelicula._peliculas.append(self)
    
    def prestar(self):
        self.prestamos += 1
        self.cantidad_disponible -= 1
    
    def ver(self):
        pass
    
    @classmethod
    def get_peliculas(cls):
        return cls._peliculas