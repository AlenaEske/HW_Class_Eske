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