class Car():
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def move(self):
        print("A car moves on 4 wheels on dry land")

class train():
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model

    def move(self):
        print("A train moves on tracks.")

class plane():
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model

    def move(self):
        print("A plane moves through the air.")

c=Car("Volvo", "Forward")
t=train("Trainer", "12")
p=plane("Boeing", "B747")

for vehicle in (c,t,p):
    vehicle.move()
    
