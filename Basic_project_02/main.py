from unicodedata import name
import mysql.connector
from models.Student import Student
from models.Undergraduate import Undergraduate

my_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "basic_project_02" # Indicar que base de datos se va a usar
)

my_cursor = my_db.cursor()
create_database = "CREATE DATABASE IF NOT EXISTS basic_project_02"
my_cursor.execute(create_database)    


create_table_students = """CREATE TABLE IF NOT EXISTS students(
    CC INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    lastname VARCHAR (255),
    undergraduate VARCHAR (100),
    subjects VARCHAR (255)
)"""
my_cursor.execute(create_table_students)  



if __name__ == "__main__":

    math = Undergraduate("Mathematics", 140)
    fisic = Undergraduate("Fisic", 176)

    s1 = Student(1,"Jose", "Perez", math)
    s2 = Student(2,"Paolo", "Martines", math)
    s3 = Student(3,"Johana", "Sierra", fisic)
    s4 = Student(4,"Jose", "Echavarria", fisic)
    
    my_db.close()