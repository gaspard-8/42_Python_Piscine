#!/usr/bin/env python3

class Plant:
    def __init__(self, Name, Height, Age):
        self.Name = Name
        self.Height = Height
        self.Age = Age
        pass


def print_plant(plant: Plant) -> None:
    print(f"{plant.Name}: {plant.Height}cm, {plant.Age} days old")


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
