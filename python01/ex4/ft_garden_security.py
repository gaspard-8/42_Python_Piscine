#!/usr/bin/env python3

class SecurePlant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age
        pass

    def set_height(self, height=0) -> bool:
        if height < 0:
            print(f"Invalid set_height attempted : height={height} [REJECTED]")
            return (False)
        else:
            self.height = height
            return (True)

    def set_age(self, age=0) -> bool:
        if age < 0:
            print(f"Invalid set_age attempted : age = {age} [REJECTED]")
            return (False)
        else:
            self.age = age
        return (True)

    def get_height(self):
        if self.height < 0:
            print("Security : Negative height rejected")
        else:
            print(f"Height of {self}: {self.height}")

    def get_age(self):
        if self.age < 0:
            print("Security : Negative age rejected")
        else:
            print(f"Age of {self}: {self.age}")

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main():
    plant = SecurePlant("Thomas", 180, 26)
    print(f"Created: {plant.name} ({plant.height}cm, {plant.age} days)")
    if (plant.set_height(190)):
        print(f"Height successfully modified to {plant.height}")
    if (plant.set_age(-1)):
        print(f"height successfully modified to {plant.height}")


if __name__ == "__main__":
    main()
