class Student:
    name = ""
    age = 0
    gender = ""
    score = 0

    def introduction(self):
        print(f"Név: {self.name},\nKor: {self.age},\nPontszám: {self.score}")




tivadar = Student()

tivadar.name = "El Tivadar"
tivadar.age = 16
tivadar.gender = "male"
tivadar.score = 20

tivadar.introduction()