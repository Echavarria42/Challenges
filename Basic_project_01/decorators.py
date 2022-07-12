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


list_question = []
def only(comprobar):
    def comprobar_unicidad(self):
        aux = str(type(self))[15:]
        if "Client" in aux:
            from models.Client import Client
            list_question = Client.get_clients()
        elif "Movie" in aux:
            from models.Movie import Movie
            list_question = Movie.get_movies()
        else:
            from models.Book import Book
            list_question = Book.get_books()
        
        for unidad in list_question:
            if unidad.__str__() == self.__str__():
                return "USUARIO YA REGISTRADO"

        self.save()
        return comprobar(self)


    
    return comprobar_unicidad