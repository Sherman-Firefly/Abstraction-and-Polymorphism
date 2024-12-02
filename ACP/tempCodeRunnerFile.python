from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    @abstractmethod
    def fuel_type(self):
        pass
    
    @abstractmethod
    def max_speed(self):
        pass

class Ferrari(Car):
    def __init__(self, brand, model):
        super().__init__(brand,model)
    
    def fuel_type(self):
        return "Premium fuel"
    
    def max_speed(self):
        return 400 #km/h
    
    
class BMW(Car):
    def __init__(self, brand, model):
        super().__init__(brand,model)
    
    def fuel_type(self):
        return "Premium gasoline"
    
    def max_speed(self):
        return 249 
    
f=Ferrari("Ferrari", "M88 Pista")
b=BMW("BMW", "M5")

for vehicle in (f,b):
   print(f"{vehicle.brand} {vehicle.model} - Fuel Type: {vehicle.fuel_type()}, Max Speed: {vehicle.max_speed()} km/h")