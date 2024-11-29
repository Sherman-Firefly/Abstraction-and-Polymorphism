class Vehicle():
    def __init__(self, brand, model):
        self.model=model
        self.brand=brand
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("A car moves on 4 wheels on dry land")

class train(Vehicle):
    def move(self):
        print("A train moves on tracks.")

class plane(Vehicle):
    def move(self):
        print("A plane moves through the air.")

c=Car("Volvo", "Forward")
t=train("Trainer", "12")
p=plane("Boeing", "B747")

for v in (c,t,p):
    v.move()
    print(v.brand, v.model)
    
