class Engine:
    def __init__(self, volume:float, horse_power:float, torque:float):
        self.volume = volume
        self.horse_power = horse_power
        self.torque = torque

class Transmission:
    def __init__(self, type:str = "automatic"):
        self.type = type

class Drivable:
    def __init__(self, wheels_count:int, engine:Engine, seats_count:int):
        self.wheels_count = wheels_count
        self.engine = engine
        self.seats_count = seats_count

class Car(Drivable):
    def __init__(self, transmission:Transmission):
        self.transmission = transmission

class Bicycle(Drivable):
    def __init__(self):
        self.engine = None

m111 = Engine(4.3, 330, 400)

simple_drivable = Drivable(0, None, 0)
mercedes = Car(4, m111, 5)
bicycle = Bicycle(2, 1)

print(f"Engine:\n\tVolume:{m111.volume}\n\tHP:{m111.horse_power}\n\tTorque:{m111.torque}")
print(f"Car:\n\tWheels:{mercedes.wheels_count}\n\tEngine:{mercedes.engine.volume, mercedes.engine.horse_power}\n\tSeats:{mercedes.seats_count}")
