def only(comprobar):
    def comprobar_unicidad(cc):
        from main import my_cursor
        exists_client = """ SELECT COUNT(name) FROM students
WHERE CC = %s """
        value = (cc,)
        my_cursor.execute(exists_client, value)
        for cursor in my_cursor:
            if 0 in cursor:
                return comprobar(cc)


    
    return comprobar_unicidad
