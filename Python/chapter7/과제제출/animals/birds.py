class Eagle:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __str__(self):
        return f"이 독수리의 이름은 {self.name}이고, 종은 {self.species}입니다."