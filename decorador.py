def decoradorSaludar(respuesta):
    def saluda():
        print(f"Hola {respuesta()}")
    
    return saluda

def preguntarNombre():
    return input("¿Cual es tu nombre? : ")


a = decoradorSaludar(preguntarNombre)
a()