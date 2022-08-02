import pandas as pd

import mysql.connector
my_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "mvm_desafio_grupal" #comenta esta linea para crear la base de datos. Luego de ser creada descomenta
)

my_cursor = my_db.cursor()

precios = pd.read_excel("Precio_kWh.xlsx")
#print(df)
for num in range(len(precios)):   
    add_precios = """ INSERT INTO precios
(estrato, tarifa_cero_CS, tarifa_mas_CS)
VALUES(%s, %s, %s) """
    values = (int(precios.iloc[num][0]), float(precios.iloc[num][1]), float(precios.iloc[num][2]))
    my_cursor.execute(add_precios, values)
    my_db.commit()
    