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