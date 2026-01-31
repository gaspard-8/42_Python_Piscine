#!/usr/bin/env python3
class Plant:
    def __init__(self, Name: str, Height: int, Age: int):
        self.Name = Name
        self.Height = Height
        self.Age = Age
        pass

    def grow(self, days: int):
        self.Height = self.Height + days

    def age(self, days: int):
        self.Age = self.Age + days

    def get_info(self):
        print(f"{self.Name}: {self.Height}cm, {self.Age} days old")


class Flower(Plant):
    def __init__(self, Name, Height, Age, Color):
        super().__init__(Name, Height, Age)
        self.Color = Color
        pass

    def bloom(self):
        print(f"{self.Name} is blooming beautifully!")

    def get_info(self):
        print(f"{self.Name} (Flower): {self.Height}cm, {
            self.Age} days old, color : {self.Color}")


class Tree(Plant):
    def __init__(self, Name, Height, Age, TrunkDiameter):
        super().__init__(Name, Height, Age)
        self.TrunkDiameter = TrunkDiameter
        pass

    def produce_shade(self):
        shade = (self.Height / 100) * (self.TrunkDiameter / 5)
        print(f"{self.Name} provides{shade} square meters of shade")

    def get_info(self):
        print(f"{self.Name} (Tree): {self.Height}cm, {
            self.Age} days old,  {self.TrunkDiameter} squares meters of shade")


class Vegetable(Plant):
    def __init__(self, Name, Height, Age, harvest_season, nutritional_value):
        super().__init__(Name, Height, Age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        pass

    def bloom(self):
        shade = (self.Height / 100) * (self.TrunkDiameter / 5)
        print(f"{self.Name} provides{shade} square meters of shade")

    def get_info(self):
        print(f"{self.Name} (Vegetablee): {self.Height}cm, {
            self.Age} days old,  {self.harvest_season} harvest")


def main():
    print("=== Garden Plant type ===")
    rose = Flower("Rose", 25, 30, "red")
    violette = Flower("Violette", 15, 31, "purple")
    oak = Tree("Oak", 500, 1825, 50)
    olivier = Tree("Olivier", 400, 1400, 20)
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    brocolli = Vegetable("Broccoli", 50, 30, "autumn", "iron")
    rose.get_info()
    violette.get_info()
    oak.get_info()
    olivier.get_info()
    tomato.get_info()
    brocolli.get_info()


if __name__ == "__main__":
    main()
