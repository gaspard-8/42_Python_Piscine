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

    def score(self) -> int:
        return self.__height


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
        print(f"{self.get_name()} is blooming beautifully!")

    def get_info(self):
        print(f"{self.get_name()} (Flower):"
              f" {self.get_height()}cm,{self.get_age()}"
              f" days old, color : {self.__color}")

    def score(self) -> int:
        return 4 * self.get_height()


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, age, color, prize_points):
        super().__init__(name, height, age, color)
        self.__prize_points = prize_points

    def get_prize_points(self) -> int:
        return self.__prize_points

    def set_prize_points(self, prize_points: int):
        if prize_points < 0:
            raise ValueError
        else:
            self.__prize_points = prize_points

    def set_prize_poitns(self, prize_points: int):
        self.set_prize_points(prize_points)

    def score(self) -> int:
        return 10 * self.get_height()


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.__trunk_diameter = trunk_diameter
        pass

    def produce_shade(self):
        shade = (self.get_height() / 100) * (self.__trunk_diameter / 5)
        print(f"{self.get_name()} provides {shade} square meters of shade")

    def get_info(self):
        print(f"{self.get_name()} (Tree): {self.get_height()}cm, "
              f"{self.get_age()} days old,"
              f" {self.__trunk_diameter} square meters of shade")


class Garden:
    def __init__(self, name: str, plants: list[Plant]):
        self.__name = name
        self.__list_of_plants = plants

    def add_plants(self, plants: list[Plant]):
        for plant in plants:
            self.__list_of_plants.append(plant)
            plant.set_garden

    def get_nb_of_plants(self) -> int:
        i = 0
        for plants in self.__list_of_plants:
            i += 1
        return i

    def get_info(self):
        print(f"===== Welcome to {self.__name} Garden =====")
        print(f"{self.__name} Garden has {self.get_nb_of_plants()} plants")
        for plant in self.__list_of_plants:
            plant.get_info()
        print("Plant types : ")

        if self.get_nb_of_reg_plants() > 0:
            print(f"{self.get_nb_of_reg_plants()} regular plant(s)")
        if self.get_nb_of_tree() > 0:
            print(f"{self.get_nb_of_tree()} tree(s)")
        if self.get_nb_of_flower() > 0:
            print(f"{self.get_nb_of_flower()} flower(s)")
        if self.get_nb_of_prize_flowers() > 0:
            print(f"{self.get_nb_of_prize_flowers()} prize flower(s)")
        print()
        print("===== Please come visit again ! =====")
        print()

    def age(self, days: int):
        for plant in self.__list_of_plants:
            plant.age(days)

    def grow(self, size: int):
        for plant in self.__list_of_plants:
            plant.grow(size)

    def get_nb_of_reg_plants(self) -> int:
        nb = 0
        for plants in self.__list_of_plants:
            if isinstance(plants, Plant):
                nb += 1
        return nb

    def get_nb_of_tree(self) -> int:
        nb = 0
        for plants in self.__list_of_plants:
            if isinstance(plants, Tree):
                nb += 1
        return nb

    def get_nb_of_flower(self) -> int:
        nb = 0
        for plants in self.__list_of_plants:
            if isinstance(plants, FloweringPlant):
                nb += 1
        return nb

    def get_nb_of_prize_flowers(self) -> int:
        nb = 0
        for plants in self.__list_of_plants:
            if isinstance(plants, PrizeFlower):
                nb += 1
        return nb

    def score(self):
        score = 0
        for plant in self.__list_of_plants:
            score += plant.score()
        return score


class GardenManager:
    class GardenStats:
        @staticmethod
        def area(a: int, b: int) -> int:
            return (a*b)

    def __init__(self, gardens: list[Garden]):
        self.__list_of_gardens = gardens

    def add_gardens(self, gardens: list[Garden]):
        self.__list_of_gardens = self.__list_of_gardens + gardens

    def nb_of_gardens(self) -> int:
        i = 0
        for garden in self.__list_of_gardens:
            i += 1
        return i

    def get_info(self):
        print(f"Garden manager report for {self.nb_of_gardens()} garden(s)")
        for garden in self.__list_of_gardens:
            garden.get_info()

    @classmethod
    def create_garden_network(cls, garden_names: list[str]):
        manager = cls([])
        for names in garden_names:
            manager.add_gardens([Garden(names, [])])
        return manager


def main():
    print("=" * 60)
    print("DEMONSTRATION OF GARDEN ANALYTICS SYSTEM")
    print("=" * 60)

    print("\n--- Plant classes ---")
    basic_plant = Plant("Basil", 15, 30)
    flower = FloweringPlant("Rose", 25, 45, "Red")
    prize_flower = PrizeFlower("Orchid", 30, 60, "Purple", 100)
    tree = Tree("Oak", 500, 365, 50)
    for plant in [basic_plant, flower, prize_flower, tree]:
        plant.get_info()

    basic_plant.grow(5)
    basic_plant.age(10)
    print(f"{basic_plant.get_name()} after updates: "
          f"{basic_plant.get_height()}cm, {basic_plant.get_age()} days")

    flower.bloom()
    flower.set_color("Pink")
    print(f"{flower.get_name()} color: {flower.get_color()}")

    prize_flower.set_prize_points(150)
    print(f"{prize_flower.get_name()} prize points: "
          f"{prize_flower.get_prize_points()}")
    tree.produce_shade()

    print("\n--- Plant scores ---")
    for plant in [basic_plant, flower, prize_flower]:
        print(f"{plant.get_name()} score: {plant.score()}")

    print("\n--- Gardens ---")
    garden1 = Garden("Sunny Garden", [
        Plant("Tomato", 40, 50),
        FloweringPlant("Tulip", 20, 35, "Yellow"),
        FloweringPlant("Sunflower", 150, 60, "Yellow")
    ])
    garden2 = Garden("Forest Garden", [
        Tree("Pine", 800, 730, 80),
        PrizeFlower("Blue Rose", 35, 90, "Blue", 200),
        Plant("Fern", 25, 40)
    ])
    garden1.get_info()
    garden2.get_info()

    garden1.grow(10)
    garden1.age(7)
    garden1.add_plants([
        FloweringPlant("Daisy", 15, 20, "White"),
        Plant("Cactus", 10, 100)
    ])
    print(f"Sunny Garden now has {garden1.get_nb_of_plants()} plants")
    print(f"Sunny Garden score: {garden1.score()}")

    print("\n--- Garden manager + stats ---")
    manager = GardenManager([garden1, garden2])
    manager.add_gardens([Garden("Herb Garden", [
        Plant("Mint", 12, 25),
        Plant("Oregano", 8, 30)
    ])])
    print(f"Manager oversees {manager.nb_of_gardens()} gardens")
    manager.get_info()

    network_manager = GardenManager.create_garden_network([
        "Community Garden", "Botanical Garden", "Rooftop Garden"
    ])
    print(f"Network gardens: {network_manager.nb_of_gardens()}")

    sample_area = GardenManager.GardenStats.area(12, 8)
    print(f"Sample area (12 x 8): {sample_area}")

    print("\n" + "=" * 60)
    print("DEMONSTRATION COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()
