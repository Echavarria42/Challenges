class Movie:
    _movies = []

    def __init__(self, name, year, duration_min, age_allowed, gender, sale_price, rental_price, available_quantity ):
        self.name = name
        self.year = year
        self.duration_min = duration_min
        self.age_allowed = age_allowed
        self.gender = gender
        self.loans = 0
        self.sale_price = sale_price
        self.rental_price = rental_price
        self.available_quantity = available_quantity 
        Movie._movies.append({
            "name" : name,
            "year" : year,
            "duration_min" : duration_min,
            "age_allowed" : age_allowed,
            "gender" : gender,
            "loans" : self.loans,
            "sale_price" : sale_price,
            "rental_price" : rental_price,
            "available_quantity" : available_quantity 
            })

    def rent(self):
        self.loans += 1
        self.available_quantity -= 1
    
    def ver(self):
        pass

    def save_movie(self):
        from main import save_file
        import main
        main.route = "files/movies.txt"

        @save_file
        def save():
            return f"{self.name},{self.year},{self.duration_min},{self.age_allowed},{self.gender},{self.prestamos},{self.sale_price},{self.rental_price},{self.available_quantity}\n"

        return save()

    
    @classmethod
    def get_Movies(cls):
        return cls._Movies