def garden_operations():
    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError:
        print("ValueError caught")
    print("Testing ZeroDivisionError")
    a = 7
    try:
        a = a / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError : division by zero")
    print("Testing FileNotFoundError...")
    try:
        open("misssing.txt")
    except (FileNotFoundError):
        print("Caught FileNotFoundError: No such file 'missing.txt'")
    print("Testing KeyError...")
    garden = {"flower": "rose", "tree": "platane"}
    try:
        print(garden['missing_plant'])
    except KeyError:
        print("Caught Key Error: 'missing_plant'")
    print("Testing multiples errors together ...")
    try:
        int("abc")
        a = a / 0
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!")

    print("\nAll error types tested succesfully")


def main():
    garden_operations()


if __name__ == main():
    main()
