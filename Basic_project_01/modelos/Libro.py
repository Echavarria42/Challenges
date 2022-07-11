
class Libro:
    _libros = []

    def __init__(self, nombre, autor, editorial, contenido, genero, precio_venta, precio_alquiler, cant_disponible):
        self.nombre = nombre
        self.autor = autor
        self.editorial = editorial
        self.contenido = contenido
        self.genero = genero
        self.prestamos = 0
        self.precio_venta = precio_venta
        self.precio_alquiler = precio_alquiler
        self.cantidad_disponible = cant_disponible
        Libro._libros.append({
            "nombre" : nombre,
            "autor" : autor,
            "editorial" : editorial,
            "contenido" : contenido,
            "prestamos" : self.prestamos,
            "precio_venta" : precio_venta,
            "precio_alquiler" : precio_alquiler,
            "cantidad_disponible" : "cantidad_disponible"
            })
    
    def prestar(self):
        self.prestamos += 1
        self.cantidad_disponible -= 1
    
    def leer(self):
        pass

    def guardar_libro(self):
        from main import guardar_archivo
        import main
        main.ruta = f"archivos/Libros/{self.nombre}.txt"

        @guardar_archivo
        def guardar():
            return f"""{self.nombre}
{self.autor}
{self.editorial}
{self.genero}
{self.contenido}"""

        return guardar()

    @classmethod
    def get_libros(cls):
        return cls._libros