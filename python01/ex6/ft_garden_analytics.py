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
        print(f"{self.get_name()} (Flower): {self.get_height()}cm,{self.get_age()}"
              f" days old, color : {self.__color}")

    def score(self) -> int:
        return 4 * self.get_height()


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, age, color, prize_points):
        super().__init__(name, height, age, color)
        self.__prizepoints = prize_points

    def get_prize_points(self) -> int:
        return self.__prizepoints

    def set_prize_poitns(self, prize_points: int):
        if prize_points < 0:
            raise ValueError
        else:
            self.__prizepoints = prize_points

    def score(self) -> int:
        return 10 * self.get_height()


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.__trunk_diameter = trunk_diameter
        pass

    def produce_shade(self):
        shade = (self.get_height() / 100) * (self.__trunk_diameter / 5)
        print(f"{self.get_name()} provides{shade} square meters of shade")

    def get_info(self):
        print(f"{self.get_name()} (Tree): {self.get_height()}cm, "
              f"{self.get_age()} days old,"
              f" {self.__trunk_diameter} squares meters of shade")


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
        print("PLant types : ")
        print("===== Please come visit again ! =====")
        print("PLant types", end='')
        if self.get_nb_of_reg_plants() > 0:
            print(f"{self.get_nb_of_reg_plants()} regular plant(s)")
        if self.get_nb_of_tree() > 0:
            print(f"{self.get_nb_of_tree} tree(s)")
        if self.get_nb_of_flower() > 0:
            print(f"{self.get_nb_of_flower()} flower(s)")
        if self.get_nb_of_prize_flowers() > 0:
            print(f"{self.get_nb_of_prize_flowers()} prize flower(s)")

    def age(self, days: int):
        for plant in self.__list_of_plants:
            plant.age(days)

    def grow(self, size: int):
        for plant in self.__list_of_plants:
            plant.grow(size)

    def get_nb_of_reg_plants(self) -> int:
        nb = 0
        for plants in self.__list_of_plants:
            if (plants.__class__ == "Plant"):
                nb += 1
            nb += 1
        return nb

    def get_nb_of_tree(self) -> int:
        nb = 0
        for plants in self.__list_of_plants:
            if (plants.__class__ == "Tree"):
                nb += 1
            nb += 1
        return nb

    def get_nb_of_flower(self) -> int:
        nb = 0
        for plants in self.__list_of_plants:
            if (plants.__class__ == "Flower"):
                nb += 1
            nb += 1
        return nb

    def get_nb_of_prize_flowers(self) -> int:
        nb = 0
        for plants in self.__list_of_plants:
            if (plants.__class__ == "PrizeFlower"):
                nb += 1
            nb += 1
        return nb

    def score(self):
        score = 0
        for plant in self.__list_of_plants:
            score += plant.score()


class GardenManager:
    class GardenStats:
        @staticmethod
        def foo():
            pass

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
        print(f"Garden manager report for {self.nb_of_gardens} garden(s)")
        for garden in self.__list_of_gardens:
            garden.get_info()

    @classmethod
    def create_garden_network(cls, garden_names: list[str]):
        manager = cls([])
        for names in garden_names:
            manager.add_gardens([Garden(names, [])])


def main():
    print("=" * 60)
    print("DEMONSTRATION OF GARDEN ANALYTICS SYSTEM")
    print("=" * 60)

    # === 1. Creating different types of plants ===
    print("\n--- 1. Creating Plants ---")
    basic_plant = Plant("Basil", 15, 30)
    basic_plant.get_info()

    flower = FloweringPlant("Rose", 25, 45, "Red")
    flower.get_info()

    prize_flower = PrizeFlower("Orchid", 30, 60, "Purple", 100)
    prize_flower.get_info()

    tree = Tree("Oak", 500, 365, 50)
    tree.get_info()

    # === 2. Demonstrating plant methods ===
    print("\n--- 2. Plant Growth and Aging ---")
    print(f"Before growth: {basic_plant.get_name()} is {basic_plant.get_height()}cm")
    basic_plant.grow(5)
    print(f"After growing 5cm: {basic_plant.get_name()} is {basic_plant.get_height()}cm")

    print(f"Before aging: {basic_plant.get_name()} is {basic_plant.get_age()} days old")
    basic_plant.age(10)
    print(f"After aging 10 days: {basic_plant.get_name()} is {basic_plant.get_age()} days old")

    # === 3. Demonstrating flowering plant features ===
    print("\n--- 3. Flowering Plant Features ---")
    flower.bloom()
    print(f"Color: {flower.get_color()}")
    flower.set_color("Pink")
    print(f"New color: {flower.get_color()}")

    # === 4. Demonstrating prize flower features ===
    print("\n--- 4. Prize Flower Features ---")
    print(f"Prize points: {prize_flower.get_prize_points()}")
    prize_flower.set_prize_poitns(150)
    print(f"Updated prize points: {prize_flower.get_prize_points()}")

    # === 5. Demonstrating tree features ===
    print("\n--- 5. Tree Features ---")
    tree.produce_shade()

    # === 6. Demonstrating scoring system ===
    print("\n--- 6. Plant Scoring System ---")
    print(f"Basic plant ({basic_plant.get_name()}) score: {basic_plant.score()}")
    print(f"Flowering plant ({flower.get_name()}) score: {flower.score()}")
    print(f"Prize flower ({prize_flower.get_name()}) score: {prize_flower.score()}")

    # === 7. Creating gardens ===
    print("\n--- 7. Creating Gardens ---")
    garden1_plants = [
        Plant("Tomato", 40, 50),
        FloweringPlant("Tulip", 20, 35, "Yellow"),
        FloweringPlant("Sunflower", 150, 60, "Yellow")
    ]
    garden1 = Garden("Sunny Garden", garden1_plants)

    garden2_plants = [
        Tree("Pine", 800, 730, 80),
        PrizeFlower("Blue Rose", 35, 90, "Blue", 200),
        Plant("Fern", 25, 40)
    ]
    garden2 = Garden("Forest Garden", garden2_plants)

    # === 8. Demonstrating garden methods ===
    print("\n--- 8. Garden Information ---")
    garden1.get_info()
    print()
    garden2.get_info()

    # === 9. Garden growth and aging ===
    print("\n--- 9. Garden-wide Growth and Aging ---")
    print(f"Garden1 has {garden1.get_nb_of_plants()} plants")
    print("Growing all plants by 10cm...")
    garden1.grow(10)
    print("Aging all plants by 7 days...")
    garden1.age(7)
    garden1.get_info()

    # === 10. Adding plants to existing garden ===
    print("\n--- 10. Adding Plants to Garden ---")
    new_plants = [
        FloweringPlant("Daisy", 15, 20, "White"),
        Plant("Cactus", 10, 100)
    ]
    print(f"Before adding: {garden1.get_nb_of_plants()} plants")
    garden1.add_plants(new_plants)
    print(f"After adding: {garden1.get_nb_of_plants()} plants")

    # === 11. Creating GardenManager ===
    print("\n--- 11. Garden Manager System ---")
    manager = GardenManager([garden1, garden2])
    print(f"Manager oversees {manager.nb_of_gardens()} gardens")

    # === 12. Adding gardens to manager ===
    print("\n--- 12. Adding More Gardens to Manager ---")
    garden3 = Garden("Herb Garden", [
        Plant("Mint", 12, 25),
        Plant("Oregano", 8, 30)
    ])
    manager.add_gardens([garden3])
    print(f"Now managing {manager.nb_of_gardens()} gardens")

    # === 13. Full manager report ===
    print("\n--- 13. Full Garden Manager Report ---")
    manager.get_info()

    # === 14. Creating garden network ===
    print("\n--- 14. Creating Garden Network ---")
    network_manager = GardenManager.create_garden_network([
        "Community Garden",
        "Botanical Garden",
        "Rooftop Garden"
    ])
    print("Garden network created successfully!")

    print("\n" + "=" * 60)
    print("DEMONSTRATION COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()
