#качина типізація
class Duck:
    def quack(self):
        print("Кря")

class Person:
    def quack(self):
         print("Крякає по людськи")

def make_it_quack(obj):
    obj.quack()

duck = Duck()
person = Person()
make_it_quack(duck)
make_it_quack(person)

#Статичний та динамічний поліморфізм

#статичний поліморфізм
def add(x, y)
    return x + y
result1 = add(1 ,4)
result2 = add("Hello", "World")
print(result1, result2)

#динамічний поліморфізм
class Animal:
    def make_sound(self):
        pass
class Dog(Animal):
    def make_sound(self):
        return"Bark!"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

def animal_speak(animal):
    return animal.make_sound()

dog, cat, = Dog(), Cat()
result1 = animal_speak(dog)
result2 = animal_speak(cat)
print(result1, result2)

