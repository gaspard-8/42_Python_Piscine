class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age
        pass

    def grow(self, days: int):
        self.height = self.height + days

    def age(self, days: int):
        self.age = self.age + days

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        pass

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")

    def get_info(self):
        print(f"{self.name} (Flower): {self.height}cm,{self.age}"
              f" days old, color : {self.color}")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        pass

    def produce_shade(self):
        shade = (self.height / 100) * (self.trunk_diameter / 5)
        print(f"{self.name} provides{shade} square meters of shade")

    def get_info(self):
        print(f"{self.name} (Tree): {self.height}cm, {self.age} days old,"
              f" {self.trunk_diameter} squares meters of shade")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        pass

    def bloom(self):
        shade = (self.height / 100) * (self.trunk_diameter / 5)
        print(f"{self.name} provides{shade} square meters of shade")

    def get_info(self):
        print(f"{self.name} (Vegetablee): {self.height}cm, {self.age}"
              f" days old, {self.harvest_season} harvest")
