class vehicle:
    def __init__(self, brand):
        self.brand = brand
    def move(self):
        return f"{self.brand} is moving"
class car(vehicle):
    def honk(self):
        return "beep beep!"
class bus(vehicle):
    def honk(self):
        return "honk honk!"
for vehicles in (car("Toyota"), bus("Mercedes")):
    print(vehicles.move() + " " + vehicles.honk())