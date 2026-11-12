class Plane:
    def __init__(self, name="", volume=0, passengers=0, year=0, country=""):
        self.__volume = volume
        self.__name = name
        self.__passengers = passengers

        self.year = year
        self.country = country

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    def get_number(self):
        return self.__passengers

    def set_number(self, value):
        self.__passengers = value

    def get_volume(self):
        return self.__volume

    def set_volume(self, value):
        self.__volume = value

    def __str__(self):
        return f"Plane: {self.__name}, {self.__volume}"

    def __repr__(self):
        return f"Plane('{self.__name}', {self.__volume}, {self.__passengers})"

    def __del__(self):
        print(f"Object {self.__name} deleted")


def main():
    plane1 = Plane("Boeing 747", 183380, 180, 2000, "Ukraine")
    plane2 = Plane("Airbus A380", 320000, 200, 2003, "Poland")
    plane3 = Plane("Cessna 172", 212, 322, 1996, "USA")
    plane4 = Plane(country="Mexico")

    for plane in [plane1, plane2, plane3, plane4]:
        print(f"Name: {plane.get_name()}, "
              f"Volume: {plane.get_volume()}, "
              f"Number: {plane.get_number()}, "
              f"Year: {plane.year}, "
              f"Country: {plane.country}")
        print(plane)
        print(repr(plane))
        print()


main()