class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def __str__(self):
        return f"이 개의 이름은 {self.name}이고, 종은 {self.breed}입니다."