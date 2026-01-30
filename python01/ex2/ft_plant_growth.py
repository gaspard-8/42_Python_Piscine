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
    print(f"Growth this week: +{plant.Height - 25}cm")


if __name__ == "__main__":
    main()
