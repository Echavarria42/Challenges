#validar cedula en base

import mysql.connector
my_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "mvm_desafio_grupal" #comenta esta linea para crear la base de datos. Luego de ser creada descomenta
)

my_cursor = my_db.cursor()

if __name__=="__main__":
    id=int(input("Ingrese el ID: "))
    busqueda_cliente = f"""SELECT COUNT(*) FROM mvm_desafio_grupal.clientes
WHERE cedula = {id};
    """
    my_cursor.execute(busqueda_cliente)  
    count = sum([sum(i) for i in my_cursor])

    #count=(BD_C.CEDULA.values ==id).sum()
    if count == 0:
        print ("Lo sentimos, este usuario no se encuentra en nuestras bases de datos")
    else:
        encontrar_usuario = f"""SELECT * FROM mvm_desafio_grupal.clientes
WHERE cedula = {id};
    """
        my_cursor.execute(encontrar_usuario)  
        usuario = {}
        for i in my_cursor:
            usuario["cedula"] = i[0]
            usuario["nombre_apellido"] = i[1]
            usuario["estrato"] = i[2]
            usuario["consumo"] = i[3]

        encontrar_tarifas = f"""SELECT * FROM mvm_desafio_grupal.precios
WHERE estrato = {usuario["estrato"]};
    """ 
        my_cursor.execute(encontrar_tarifas)  
        tarifas = {}
        for i in my_cursor:
            tarifas["tarifa_cero_CS"] = i[1]
            tarifas["tarifa_mas_CF"] = i[2]

        subs=0
        no_subs=0
        if usuario["consumo"]>173:
            subs = 173
            no_subs=usuario["consumo"]-173
        else:
            subs = usuario["consumo"]

        pago_subs=subs*tarifas["tarifa_cero_CS"]
        pago__no_subs = no_subs*tarifas["tarifa_mas_CF"]
     
        print("El cliente "+ usuario["nombre_apellido"])
        print("consumió un total de: "+str(usuario["consumo"])+"kWh.")
        print("Equivalentes a un pago de "+str(round(pago_subs,3))+" por kWh subsidiados y "+str( round( pago__no_subs,3) )+" por consumo no subsidiado")
        print("Para un total de "+str(round(pago__no_subs+pago_subs,3)))