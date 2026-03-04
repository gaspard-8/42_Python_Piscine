
def main():
    print("=== Import Transmutation Mastery ===")
    print()

    import alchemy
    print("Meethod 1 - Full module import:")
    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")
    print()

    from alchemy.elements import create_water
    print("Method 2 - Specific function import:")
    print(f"create_water(): {create_water()}")
    print()

    from alchemy.potions import healing_potion as heal
    print("Method 3 - Aliased import:")
    print(f"heal(): {heal()}")
    print()

    from alchemy.elements import create_earth, create_fire
    from alchemy.potions import strength_potion
    print("Method 4 - Multiple imports:")
    print(f"create_earth(): {create_earth()}")
    print(f"create_fire(): {create_fire()}")
    print(f"strength_potion(): {strength_potion()}")

    print()
    print("All import transmutation methods mastered")


if __name__ == "__main__":
    main()
