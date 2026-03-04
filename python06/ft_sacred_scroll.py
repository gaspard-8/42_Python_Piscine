#!/usr/bin/env python3

import alchemy


def main():
    print("=== Sacred Scroll Mastery ===")
    print()
    print("Testing direct module access:")
    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")
    print(f"alchemy.elements.create_water(): "
          f"{alchemy.elements.create_water()}")
    print(f"alchemy.elements.create_earth(): "
          f"{alchemy.elements.create_earth()}")
    print(f"alchemy.elements.create_air(): "
          f"{alchemy.elements.create_air()}")
    print()
    print("Testing package-level access (controlled by __init__.py):")
    try:
        print("alchemy.create_fire():", end=" ")
        print(alchemy.create_fire())
    except AttributeError as e:
        print(e)
    try:
        print("alchemy.create_water():", end=" ")
        print(alchemy.create_water())
    except AttributeError as e:
        print(e)
    try:
        print("alchemy.create_earth():", end=" ")
        print(alchemy.create_earth())
    except AttributeError:
        print("AttributeError - not exposed")
    try:
        print("alchemy.create_air():", end=" ")
        print(alchemy.create_air())
    except AttributeError:
        print("AttributeError - not exposed")

    print()
    print("Package metadata:")
    print("Version: 1.0.0")
    print("Author: Master Pythonicus")
    return


if __name__ == "__main__":
    main()
