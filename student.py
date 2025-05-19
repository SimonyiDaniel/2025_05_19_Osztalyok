class Student:
    name = ""
    age = 0
    gender = ""
    score = 0

    def introduction(self):
        print(f"Név: {self.name}\nKor: {self.age}\nPontszám: {self.score}")
    
    def studied(self, points):
        self.score += points





tivadar = Student()

tivadar.name = "El Tivadar"
tivadar.age = 16
tivadar.gender = "male"
tivadar.score = 20

tivadar.introduction()
tivadar.studied(12)
tivadar.introduction()