class Undergraduate:
    def __init__(self, name, credits):
        self.name = name
        self.credits = credits


class Subject:
    def __init__(self, name, credits, faculty):
        self.name = name
        self.credits = credits
        self.faculty = faculty