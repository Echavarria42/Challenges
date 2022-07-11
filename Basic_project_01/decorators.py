route = ""
def save_file(objeto_registrado):

    def registrar_objeto(self):
        aux = str(type(self))[15:]
        if "Client" in aux:
            route = "files/clients.txt"
        elif "Movie" in aux:
            route = "files/movies.txt"
        else:
            route = f"files/Books/{self.name}.txt"

        with open(route, "a+") as ar:
            ar.write(objeto_registrado(self))

    return registrar_objeto
