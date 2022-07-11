from modelos.Pelicula import Pelicula
from modelos.Libro import Libro
from modelos.Cliente import Cliente


ruta = ""
def guardar_archivo(objeto_registrado):

    def registrar_objeto():
        with open(ruta, "a+") as ar:
            ar.write(objeto_registrado())
    return registrar_objeto



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
    c1 = Cliente(1000295140, "Mateo", "echavarria.0042@gmail.com", 123123123)
    c1.guardar_cliente()

    p1 = Pelicula("Nemo", 2004, 120, 8, "familiar", 50000, 2000, 5)
    p1.guardar_pelicula()

    l1 = Libro("Poemas", "Mateo Echavarria", "Independiente", "Y nuestras almas vueltas una sola como si nos hubieran forjado con el mismo odio", "poesia", 20000, 2000, 1)
    l1.guardar_libro()