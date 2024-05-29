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