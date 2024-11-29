from abc import  ABC
class Animal(ABC):
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("Humans can walk on two feet.")

class Snake(Animal):
    def move(self):
        print("Snakes slither around the ground.")

class Dog(Animal):
    def move(self):
        print("Dogs walk on 4 legs.")

class Bird(Animal):
    def move(self):
        print("Birds can walk on the ground as well as fly with their wings (except penguins and chicken)")

h=Human()
h.move()

s=Snake()
s.move()

d=Dog()
d.move()

b=Bird()
b.move()