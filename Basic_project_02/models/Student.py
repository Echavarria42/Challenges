import imp
from unicodedata import name
from decorators import only
from models.Undergraduate import Undergraduate

class Student:
    def __init__(self, CC : int, name : str, lastname : str, undergraduate : Undergraduate):
        self.CC = CC
        self.name = name
        self.lastname = lastname
        self.undergraduate = undergraduate
        self.subjects = None

        from main import my_cursor, my_db
        @only
        def only_student(CC):
            add_student = """ INSERT INTO students
(CC, name, lastname, undergraduate, subjects)
VALUES(%s, %s, %s, %s, %s) """
            values = (self.CC, self.name, self.lastname, self.undergraduate.name , self.subjects)
            my_cursor.execute(add_student, values)
            my_db.commit()
        
        only_student(CC)
    
    def update_info(self, **kwargs):
        from main import my_cursor, my_db
        update_student = """ UPDATE students
SET name = %s, lastname = %s, undergraduate = %s
WHERE CC = %s """
        values = [ arg if arg != None else self.assignment(key) for key , arg in kwargs.items() ] + [self.CC]
        my_cursor.execute(update_student, values)
        my_db.commit()


        self.name = values[0]
        self.lastname = values[1]
        self.undergraduate = values[2]


    def assignment(self, value):
        if value == "name":
            return self.name
        elif value == "lastname":
            return self.lastname
        else:
            return self.undergraduate.name
    
    def undergraduate_cancellation(self):
        from main import my_cursor, my_db
        print("unattached student")
        add_student = """ DELETE FROM students
WHERE CC = %s """
        value = (self.CC,)
        my_cursor.execute(add_student, value)
        my_db.commit()
