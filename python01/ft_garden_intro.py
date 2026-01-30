#!/usr/bin/env python3

def print_plant(plant_name: str, plant_height: int, plant_age: int) -> None:
    print("Plant:", plant_name)
    print(f"Height: {plant_height}cm")
    print("Age:", plant_age, "days\n")


def main():
    print("=== Welcome to My Garden ===")
    print_plant("Rose", 25, 30)
    print("=== End of Program ===")


if __name__ == "__main__":
    main()
