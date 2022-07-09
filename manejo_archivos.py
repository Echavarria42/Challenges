def AgregarPersona(archivo):
    nombre = input("Nombre: ")
    edad   = input("Edad  : ")
    email  = input("Email : ")

    fila = f"\n{nombre} - Edad {edad} - {email}"
    archivo.write(fila)
    print("----- P E R S O N A   A G R E G A D A -----\n")

ruta = "archivos/manejo_archivos.txt"
print("""R E G I S T R A R   P E R S O N A S
""")
with open(ruta, "a+") as personas:
    agregar = -1
    while agregar != 0:    
        agregar = int(input("[0] Salir - [1] registrar - [2] Visualizar Personas\n"))
        
        if agregar == 1:
            AgregarPersona(personas)
        elif agregar == 2:
            personas.seek(0)
            print(personas.read())
        

