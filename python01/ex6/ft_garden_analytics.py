#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.__name = name
        self.__height = height
        self.__age = age
        self.__garden = None
        pass

    def set_height(self, height: int):
        if height < 0:
            raise ValueError(f"Invalid set_height"
                             f" attempted : {height} [REJECTED]")
        else:
            self.__height = height

    def set_age(self, age: int):
        if age < 0:
            raise ValueError("Negative age")
        else:
            self.__age = age

    def set_garden(self, garden):
        self.__garden = garden

    def get_name(self):
        return self.__name

    def get_height(self):
        if self.__height < 0:
            raise ValueError("Negative height")
        else:
            return self.__height

    def get_age(self) -> int:
        if self.__age < 0:
            raise ValueError("Negative age")
        else:
            return (self.__age)

    def get_garden(self):
        return ()

    def grow(self, size: int):
        self.__height = self.__height + size

    def age(self, days: int):
        self.__age = self.__age + days

    def get_info(self):
        print(f"{self.__name}: {self.__height}cm, {self.__age} days old")


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.__color = color
        pass

    def get_color(self):
        return self.__color

    def set_color(self, color: str):
        self.__color = color

    def bloom(self):
        print(f"{self.__name} is blooming beautifully!")

    def get_info(self):
        print(f"{self.__name} (Flower): {self.get_height()}cm,{self.get_age()}"
              f" days old, color : {self.__color}")


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age, color)


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.__trunk_diameter = trunk_diameter
        pass

    def produce_shade(self):
        shade = (self.__height / 100) * (self.__trunk_diameter / 5)
        print(f"{self.__name} provides{shade} square meters of shade")

    def get_info(self):
        print(f"{self.__name} (Tree): {self.__height}cm, "
              f"{self.__age} days old,"
              f" {self.__trunk_diameter} squares meters of shade")


class Garden:
    def __init__(self, name: str, plants: list[Plant]):
        self.__name = name
        self.__list_of_plants = plants

    def add_plants(self, plants: list[Plant]):
        for plant in plants:
            self.__list_of_plants.append(plant)
            plant.set_garden

    def get_nb_of_plants(self):
        return len(self.__list_of_plants)

    def get_info(self):
        print(f"===== Welcome to {self.__name} Garden =====")
        print(f"{self.__name} Garden has {self.get_nb_of_plants()} plants")
        for plant in self.__list_of_plants:
            plant.get_info()
        print("===== Please come visit again ! =====")

    def age(self, days: int):
        for plant in self.__list_of_plants:
            plant.age(days)

    def grow(self, size: int):
        for plant in self.__list_of_plants:
            plant.grow(size)


class GardenManager:
    def __init__(self, gardens: list[Garden]):
        self.__list_of_gardens = gardens

    def add_gardens(self, gardens: list[Garden]):
        self.__list_of_gardens = self.__list_of_gardens + gardens


def main():
    plants = []
    plants.append(Plant("test", 1, 1))
    garden = Garden("Mon jardin", plants)
    plants2 = []
    plants2.append(Plant("Rose", 20, 20))
    garden.add_plants(plants2)
    garden.get_info()


if __name__ == "__main__":
    main()
