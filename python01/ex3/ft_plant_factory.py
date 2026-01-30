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


def create_plant(name, height, age) -> Plant:
    plant = Plant(name, height, age)
    print(f"Created: {name} ({height}cm, {age} days)")
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
