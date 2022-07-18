from decorators import only

class Student:
    def __init__(self, CC, name, lastname):
        self.CC = CC
        self.name = name
        self.lastname = lastname
        self.subjects = None

        from main import my_cursor, my_db
        @only
        def only_student(CC):
            add_student = """ INSERT INTO students
(CC, name, lastname, subjects)
VALUES(%s, %s, %s, %s) """
            values = (self.CC, self.name, self.lastname, self.subjects)
            my_cursor.execute(add_student, values)
            my_db.commit()
        
        only_student(CC)
