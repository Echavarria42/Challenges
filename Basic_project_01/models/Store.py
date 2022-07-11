class Store:
    _clients = []
    _libros = []
    _peliculas = []

    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.money = 0

