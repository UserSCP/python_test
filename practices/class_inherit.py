class Person:
    def __init__(self, name, last,age):
        self.firstName=name
        self.lastName=last
        self.personAge=age
class Student(Person):
    def __init__(self, name, age, last,year):
        super().__init__(name,last, age)
        self.graduationyear=year
    def mostrar_info(self):
        print(f"Alumno1:\nNombre: {self.firstName}, Apellido: {self.lastName}, Edad: {self.personAge},\nAño en el que se va a graduar: {self.graduationyear}")

std1=Student("Sebastian", "Pardo", 17, 2024)
std1.mostrar_info()