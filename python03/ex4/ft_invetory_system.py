#!/usr/bin/env python3

import sys


def parse_inventory(args: list[str]) -> dict[str, int]:
    dict = {}
    for arg in args:
        try:
            (key, value) = arg.split(":")
        except ValueError:
            print(f"Invalid inventory entry : '{arg}' "
                  "entry will be ignored")
        else:
            try:
                int_value = int(value)
            except ValueError:
                print(f"Invalid inventory entry : '{arg}' "
                      "entry will be ignored")
            else:
                dict.update({key: int_value})
    return dict


def print_inventory(inv: dict[str, int]) -> None:
    print("=== Current  Inventory")
    for item in inv.items():
        print(f"{item[0]}: {item[1]} units ({(item[1]/12):.1%})")


def main():
    print("=== Inventory System Analysis")
    inventory = parse_inventory(sys.argv[1:])
    categories = {"abundant": {}, "moderate": {}, "scarce": {}}
    most_ab_item = []
    least_ab_item = []
    for item in inventory.items():
        if item[1] > 10:
            categories["abundant"].update({item[0]: item[1]})
        elif item[1] > 4:
            categories["moderate"].update({item[0]: item[1]})
        else:
            categories["scarce"].update({item[0]: item[1]})
        if not most_ab_item or item[1] > inventory[most_ab_item[0]]:
            most_ab_item = [item[0]]
        elif item[1] == inventory[most_ab_item[0]]:
            most_ab_item.append(item[0])
        if not least_ab_item or item[1] < inventory[least_ab_item[0]]:
            least_ab_item = [item[0]]
        elif item[1] == inventory[least_ab_item[0]]:
            least_ab_item.append(item[0])

    if not inventory:
        print("Inventory is empty :(")
        return
    print(f"Total items in inventory: {sum(inventory.values())}")
    print(f"Unique items types: {len(inventory.keys())}")
    print()
    print_inventory(inventory)
    print()
    print("=== Inventory stasticitcs ===")
    print(f"Most abundant: {most_ab_item} ({inventory[most_ab_item[0]]}"
          "units)")
    print(f"Least abundant: {least_ab_item} ({inventory[least_ab_item[0]]}"
          "units)")
    print()

    print("=== Item categories ===")
    if categories["abundant"]:
        print("Abundant : ", end="")
        for item in categories["abundant"].items():
            print(item, end=" ")
        print()
    if categories["moderate"]:
        print("Moderate : ", end="")
        for item in categories["moderate"].items():
            print(item, end=" ")
        print()
    if categories["scarce"]:
        print("scarce : ", end="")
        for item in categories["scarce"].items():
            print(item, end=" ")
        print()

    print()
    print("=== Management restrictions ===")
    print(f"Restock needed: {list(categories['scarce'].keys())}")
    print()
    print("=== Dictionnary Properties Demo ===")
    print(f"Dictionnary keys: {list(inventory.keys())}")
    print(f"Dictionnary values: {list(inventory.values())}")

    sample = "sword"
    print(f"Sample lookup - {sample} in inventory: {(sample in inventory)}")


if __name__ == "__main__":
    main()
