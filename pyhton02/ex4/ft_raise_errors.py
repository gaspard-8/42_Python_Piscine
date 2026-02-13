def check_plant_health(plant_name, water_level: int, sunlight_hours: int):
    if plant_name == "":
        raise ValueError("Name is empty")
    elif water_level < 1 or water_level > 10:
        raise ValueError("Water level is not in the expected [1, 10] range")
    elif sunlight_hours < 2 or sunlight_hours > 12:
        raise ValueError("sunlight hours must be bewtween 2 and 12")
    else:
        print("SUCCESS")


def test_plant_checks():
    try:
        check_plant_health("Belle Plante", 3, 3)
    except ValueError as e:
        print(e)
    try:
        check_plant_health("", 3, 3)
    except ValueError as e:
        print(e)
    try:
        check_plant_health("AA", 20, 3)
    except ValueError as e:
        print(e)
    try:
        check_plant_health("AA", 3, 40)
    except ValueError as e:
        print(e)


test_plant_checks()
