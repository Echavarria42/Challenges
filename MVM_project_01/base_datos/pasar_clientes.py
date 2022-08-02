import pandas as pd

import mysql.connector
my_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "mvm_desafio_grupal" #comenta esta linea para crear la base de datos. Luego de ser creada descomenta
)

my_cursor = my_db.cursor()

clientes = pd.read_excel("BD_Consumidores.xlsx")
#print(df)
for num in range(len(clientes)):   
    add_client = """ INSERT INTO clientes
(cedula, nombre_apellido, estrato, kWh_Consumidos)
VALUES(%s, %s, %s, %s) """
    values = (int(clientes.iloc[num][0]), str(clientes.iloc[num][1]), int(clientes.iloc[num][2]), int(clientes.iloc[num][3]))
    my_cursor.execute(add_client, values)
    my_db.commit()