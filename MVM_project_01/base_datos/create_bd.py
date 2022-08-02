import mysql.connector
my_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "mvm_desafio_grupal" #comenta esta linea para crear la base de datos. Luego de ser creada descomenta
)

my_cursor = my_db.cursor()
create_database = "CREATE DATABASE IF NOT EXISTS mvm_desafio_grupal"
my_cursor.execute(create_database)    


create_table_clientes = """CREATE TABLE IF NOT EXISTS clientes(
    cedula INT AUTO_INCREMENT PRIMARY KEY,
    nombre_apellido VARCHAR(255),
    estrato INT,
    kWh_Consumidos INT
)"""

create_table_precios = """CREATE TABLE IF NOT EXISTS precios(
    estrato INT PRIMARY KEY,
    tarifa_cero_CS DOUBLE,
    tarifa_mas_CS DOUBLE
)"""

my_cursor.execute(create_table_clientes)  
my_cursor.execute(create_table_precios)  

my_db.close()