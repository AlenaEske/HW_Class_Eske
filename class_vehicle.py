class Vehicle:
    def __init__(self, name):
        self.name = name

    def get_vehicle_type(self, wheel):
        if wheel == 2:
            return f"Это мотоцикл марки {self.name}!"
        elif wheel == 3:
            return f"Это трицикл марки {self.name}"
        elif wheel == 4:
            return f"Это автомобиль марки {self.name}"
        else:
            return f"Я таких не знаю."

    def get_vehicle_advice(self, mileage):
        if 50001 <= mileage <= 100000:
            return f"Неплохо! {self.name} можно купить!"
        elif 100001 <= mileage <= 150000:
            return f"{self.name} надо внимательно проверить!"
        elif mileage >= 150001:
            return f"{self.name} лучше не брать!"


avto_1 = Vehicle("BMW")
print(avto_1.get_vehicle_type(4))
print(avto_1.get_vehicle_advice(60000))
print()
avto_2 = Vehicle("Reno")
print(avto_2.get_vehicle_type(3))
print(avto_2.get_vehicle_advice(120000))
print()
avto_3 = Vehicle("Audi")
print(avto_3.get_vehicle_type(2))
print(avto_3.get_vehicle_advice(160000))
print()
avto_4 = Vehicle("Mercedes")
print(avto_4.get_vehicle_type(5))
