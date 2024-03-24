#Завдання 2
# Реалізуйте клас «Стадіон». Збережіть у класі: назву
#стадіону, дату відкриття, країну, місто, місткість. Реалізуйте
#методи класу для введення-виведення даних та інших
#операцій. До вже реалізованого класу «Стадіон» додайте
#необхідні перевантажені методи та оператори.

class Stadium:
    def __init__(self, name, opening_date, country, city, capacity):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def display_info(self):
        print("Стадіон:", self.name)
        print("Дата відкриття:", self.opening_date)
        print("Країна:", self.country)
        print("Місто:", self.city)
        print("Місткість:", self.capacity)

    def __str__(self):
        return f"Стадіон {self.name} розташований у місті {self.city}, {self.country}. Відкритий {self.opening_date}. Має місткість {self.capacity} осіб."

    def __eq__(self, other):
        return self.name == other.name and self.city == other.city

    def __lt__(self, other):
        return self.capacity < other.capacity

    def __add__(self, other):
        total_capacity = self.capacity + other.capacity
        return Stadium(f"{self.name} & {other.name}", "Порожній", "Сума", "Сума", total_capacity)


stadium1 = Stadium("Camp Nou", "24.09.1957", "Іспанія", "Барселона", 99354)
stadium2 = Stadium("Santiago Bernabeu", "14.12.1947", "Іспанія", "Мадрид", 81044)

stadium1.display_info()
print()

print(stadium2)
print()

print("Чи рівні стадіони?", stadium1 == stadium2)
print()

print("Стадіон з більшою місткістю:", max(stadium1, stadium2).name)
print()

merged_stadium = stadium1 + stadium2
print("Об'єднаний стадіон:", merged_stadium)

