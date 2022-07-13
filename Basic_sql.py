import mysql.connector

my_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "basic_sql" # Indicar que base de datos se va a usar
)

my_cursor = my_db.cursor()

#create_database = "CREATE DATABASE basic_sql"
#my_cursor.execute(create_database)               # Ejecutar 

#delete_database = "DROP DATABASE basicproject02"   
#my_cursor.execute(delete_database)

"""
show_databases = "SHOW DATABASES"         
my_cursor.execute(show_databases)

"""
'''
create_table = """ CREATE TABLE client(
    name VARCHAR (255),
    lastname VARCHAR (255)
) """
my_cursor.execute(create_table)
'''

#delete_table = "DROP TABLE IF EXISTS client" # Elimine la tabla si existe
#my_cursor.execute(delete_table)

my_cursor.execute("SHOW TABLES")

for item in my_cursor:
    print(item)

my_db.close() #Cerrar Base de datos