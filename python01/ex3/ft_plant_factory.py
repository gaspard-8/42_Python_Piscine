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


def create_plant(name, height, plant_age) -> Plant:
    plant = Plant(name, height, plant_age)
    print(f"Created: {name} ({height}cm, {plant_age} days)")
    return plant


def main():
    print("=== Plant Factory Output ===")
    plants = []
    plants.append(create_plant("Rose", 25, 30))
    plants.append(create_plant("Oak", 200, 365))
    plants.append(create_plant("Cactus:", 5, 90))
    plants.append(create_plant("Sunflower", 80, 45))
    plants.append(create_plant("Fern", 15, 120))
    print("\nTotal plants created: 5")


if __name__ == "__main__":
    main()
