#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, plant_age: int):
        self.name = name
        self.height = height
        self.plant_age = plant_age
        pass

    def grow(self, days: int):
        self.height = self.height + days

    def age(self, days: int):
        self.plant_age = self.plant_age + days

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.plant_age} days old")


def main():
    plant = Plant("Rose", 25, 30)
    i = 1
    print(f"=== Day {i} ===")
    plant.get_info()
    while (i < 7):
        i += 1
        plant.grow(1)
        plant.age(1)
    print(f"=== Day {i} ===")
    plant.get_info()
    print(f"Growth this week: +{plant.height - 25}cm")


if __name__ == "__main__":
    main()
