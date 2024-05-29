class Hotel:
    def __init__(self, name):
        self.name = name
    def get_hotel_of_stars(self, star):

        if star <= 2:
            included = ["трансфер"]
            return f" {self.name} - плохой отель. Там только {included}"
        elif star == 3:
            included = ["трансфер", "завтрак", "wi-fi"]
            return f"{self.name} - нормальный отель. Включено {included}. Но далеко от моря! "
        elif star == 4:
            included = ["трансфер", "шведский стол", "анимация", "wi-fi"]
            return f"{self.name} - отличный отель, включено {included}."
        else:
            return f"{self.name} - супер отель, но очень дорогой."
    def get_room_hotel(self, room):
        number_of_beds = int(input("Сколько нужно кроватей?  "))
        return f"Выберем {room} с {number_of_beds} спальными местами"
    def pack_a_suitcase(self):
        return f"Складываем чемодан"
    def attach_a_cat(self, name_cat=None):
        if name_cat is None:
            return f"Кота у нас нет"
        else:
            return f"За котом {name_cat} присмотрит сосед"
hotel_1 = Hotel("Звезда")
print(hotel_1.get_hotel_of_stars(3))
print(hotel_1.get_room_hotel("Люкс"))
print(hotel_1.attach_a_cat("Барсик"))
print()
hotel_2 = Hotel("Парадиз")
print(hotel_2.get_hotel_of_stars(4))
print(hotel_2.get_room_hotel("Полу-люкс"))
print(hotel_2.attach_a_cat())
print()
hotel_3 = Hotel("Allians Анапа")
print(hotel_3.get_hotel_of_stars(5))
print(hotel_3.get_room_hotel("Эконом"))
print(hotel_3.attach_a_cat("Пушок"))