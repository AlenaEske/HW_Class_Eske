class Vehicle:
    def __init__(self, name, mileage):
        self.name = name
        self.mileage = mileage

    def get_vehicle_type(self, wheel):
        if wheel == 2:
          return f"Это мотоцикл марки {self.name}!"
        elif wheel == 3:
            return f"Это трицикл марки {self.name}"
        else:
            return f"Это автомобиль марки {self.name}"