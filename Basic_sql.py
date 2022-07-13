import mysql.connector

my_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "basic_sql" # Indicar que base de datos se va a usar
)

my_cursor = my_db.cursor()

#sql = "CREATE DATABASE basic_sql" # Creación de base de batos
#my_cursor.execute(sql)                 # Ejecutar 

#sql = "DROP DATABASE basicproject02"    # Eliminar una base de datos
#my_cursor.execute(sql)

"""
sql = "SHOW DATABASES"                  # Mostrar todas las base de datos
my_cursor.execute(sql)

for item in my_cursor:
    print(item)

"""


my_db.close() #Cerrar Base de datos