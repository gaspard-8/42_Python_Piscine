#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        pass


def print_plant(plant: Plant) -> None:
    print("Plant:", plant.name)
    print(f"Height: {plant.height}cm")
    print("Age:", plant.age, "days")


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
