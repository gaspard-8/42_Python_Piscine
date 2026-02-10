def check_temperature(temp_str: str) -> int:
    try:
        number = int(temp_str)
    except ValueError:
        raise TypeError
    else:
        if (number >= 0 and number <= 40):
            return number
        else:
            raise ValueError


def test_temp_error(temp_str: str):
    print(f"Testing temperature: {temp_str}")
    try:
        nb_test1 = check_temperature(temp_str)
    except TypeError:
        print(f"Error: {temp_str} is not a valid number")
    except ValueError:
        if (int(temp_str) < 0):
            print(f"Error: {int(temp_str)}°C is too cold for plants (min 0°C)")
        else:
            print(f"Error: {int(temp_str)}°C is too hot for plants (min 0°C)")
    else:
        print(f"Temperature {nb_test1}°C is perfect for plants")
    print("\n")


def test_temperature_input():
    print("=== Garden Temparature Checker ===\n")
    test_temp_error("25")
    test_temp_error("abc")
    test_temp_error("100")
    test_temp_error("-50")

    print("===All test completed - program didn't crash!===")


def main():
    test_temperature_input()


# if __name__ == main():
#     main()
