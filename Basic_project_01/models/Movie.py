from decorators import save_file, only

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

        @only
        def comprobar(self):
            Movie._movies.append(self)
        comprobar(self)

    def rent(self):
        self.loans += 1
        self.available_quantity -= 1
    
    def ver(self):
        pass

    @save_file
    def save(self):      
        return f"{self.name},{self.year},{self.duration_min},{self.age_allowed},{self.gender},{self.loans},{self.sale_price},{self.rental_price},{self.available_quantity}\n"
 
    @classmethod
    def get_movies(cls):
        return cls._movies
    
    def __str__(self) -> str:
        return f"{self.name},{self.year},{self.duration_min},{self.age_allowed},{self.gender},{self.loans},{self.sale_price},{self.rental_price},{self.available_quantity}"