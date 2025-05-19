class Student:
    name = ""
    age = 0
    gender = ""
    score = 0
    mood = ""

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.score = 10

    def introduction(self):
        print(f"Név: {self.name}; Kor: {self.age}; Pontszám: {self.score}; {self.mood}")
    
    def studied(self, points):
        self.score += points





tivadar = Student("El Tivadar", 16, "male")

tivadar.introduction()
tivadar.studied(12)
tivadar.introduction()