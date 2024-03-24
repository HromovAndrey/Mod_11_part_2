#Завдання 3
# До вже реалізованого класу «Автомобіль» додайте
#необхідні перевантажені методи та оператори.
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        print("Двигун запущено.")

    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"

    def __eq__(self, other):
        return self.brand == other.brand and self.model == other.model and self.year == other.year

    def __ne__(self, other):
        return not self.__eq__(other)

car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Toyota", "Camry", 2020)

print(car1)
print(car1 == car2)
print(car1 != car2)