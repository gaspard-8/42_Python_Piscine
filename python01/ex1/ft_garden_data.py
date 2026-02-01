#!/usr/bin/env python3

class Plant:
    def __init__(self, plant_name, plant_height, plant_age):
        self.plant_name = plant_name
        self.plant_height = plant_height
        self.plant_age = plant_age
        pass


def print_plant(plant: Plant) -> None:
    print(f"{plant.plant_name}: {plant.plant_height}cm, {plant.plant_age} days old")


def main():
    print("=== Garden Plant Registry === ")
    plants = []
    plants.append(Plant("Rose", 25, 30))
    plants.append(Plant("Sunflower", 80, 45))
    plants.append(Plant("Cactus:", 15, 120))
    for i in range(3):
        print_plant(plants[i])
    print("=== End of Program ===")


if __name__ == "__main__":
    main()
