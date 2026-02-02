#!/usr/bin/env python3

class SecurePlant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.__height = height
        self.__age = age
        pass

    def set_height(self, height: int):
        if height < 0:
            raise ValueError(f"Invalid set_height"
                             f" attempted : {height} [REJECTED]")
        else:
            self.__height = height

    def set_age(self, age: int):
        if age < 0:
            raise ValueError("negative age")
        else:
            self.__age = age

    def get_height(self):
        if self._height < 0:
            print("Security : Negative height rejected")
        else:
            print(f"Height of {self}: {self.__height}")

    def get_age(self) -> int:
        if self.__age < 0:
            raise ValueError("negative age")
        else:
            print(f"Age of {self}: {self.__age}")
            return (self.__age)

    def get_info(self):
        print(f"{self.name}: {self.__height}cm, {self.__age} days old")


def main():
    print("=== Very secure Garden ===")
    plant = SecurePlant("Thomas", 180, 26)
    plant.get_info()
    height = -90
    try:
        (plant.set_height(height))
    except ValueError:
        print(f"Invalid set_age attempted : {height} [REJECTED]")
    height = 100
    try:
        (plant.set_height(height))
    except ValueError:
        print(f"Invalid set_age attempted : {height}[REJECTED]")
    else:
        print(f"Height updated to :{height}cm [OK]")


if __name__ == "__main__":
    main()
