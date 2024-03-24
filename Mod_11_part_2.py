#Завдання 4
#До вже реалізованого класу «Книга» додайте
#необхідні перевантажені методи та оператори.

class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def display_info(self):
        print(f"Назва: {self.title}, Автор: {self.author}, Жанр: {self.genre}")

    def __str__(self):
        return f"Назва: {self.title}, Автор: {self.author}, Жанр: {self.genre}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author and self.genre == other.genre

    def __ne__(self, other):
        return not self.__eq__(other)

book1 = Book("1984", "Джордж Оруелл", "Наукова фантастика")
book2 = Book("1984", "Джордж Оруелл", "Наукова фантастика")

print(book1)
print(book1 == book2)
print(book1 != book2)
