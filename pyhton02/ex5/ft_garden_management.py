class GardenError(Exception):
    def __init__(self, message: str):
        self.message = message
    pass


class PlantError(GardenError):
    def __init__(self, plant: str):
        self.message = f"A {plant} related error occured"
    pass


class WaterError(GardenError):
    pass


class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.__name = name
        self.__height = height
        self.__age = age
        self.__garden = None
        pass

    def set_height(self, height: int):
        if height < 0:
            raise ValueError(f"Invalid set_height"
                             f" attempted : {height} [REJECTED]")
        else:
            self.__height = height

    def set_age(self, age: int):
        if age < 0:
            raise ValueError("Negative age")
        else:
            self.__age = age

    def set_garden(self, garden):
        self.__garden = garden

    def get_name(self):
        return self.__name

    def get_height(self):
        if self.__height < 0:
            raise ValueError("Negative height")
        else:
            return self.__height

    def get_age(self) -> int:
        if self.__age < 0:
            raise ValueError("Negative age")
        else:
            return (self.__age)

    def get_garden(self):
        if self.__garden is None:
            raise GardenError("This plant already has a garden")
        else:
            return self.__garden

    def grow(self, size: int):
        self.__height = self.__height + size

    def age(self, days: int):
        self.__age = self.__age + days

    def check_plant_health(self, water_level: int, sunlight_hours: int):
        if self.get_name() == "":
            raise ValueError("Name is empty")
        elif water_level < 1 or water_level > 10:
            raise ValueError("Water level is not in the expected range")
        elif sunlight_hours < 2 or sunlight_hours > 12:
            raise ValueError("sunlight hours must be bewtween 2 and 12")

    def get_info(self):
        print(f"{self.__name}: {self.__height}cm, {self.__age} days old")

    def score(self) -> int:
        return self.__height


class GardenManager:
    def __init__(self, name: str, plants: list[Plant]):
        self.__name = name
        self.__list_of_plants = plants
        self.watertank = 100

    def add_plants(self, plants: list[Plant]):
        for plant in plants:
            try:
                plant.get_garden()
                self.__list_of_plants.append(plant)
            except GardenError as e:
                print(e.message)
            else:
                print(f"successfully added {plant.get_name()} ")

    def get_nb_of_plants(self) -> int:
        i = 0
        for plants in self.__list_of_plants:
            i += 1
        return i

    def age(self, days: int):
        for plant in self.__list_of_plants:
            plant.age(days)

    def grow(self, size: int):
        for plant in self.__list_of_plants:
            plant.grow(size)

    def water_plants(self):
        if self.get_nb_of_plants() * 10 > self.watertank:
            raise WaterError("Not enough water left to water the plants")
        else:
            self.grow(1)

    def water_plant(self, plant_name: str):
        count = 0
        print("Opening the Watering system")
        try:
            for plant in self.__list_of_plants:
                if plant.get_name() == plant_name:
                    if self.watertank > 10:
                        plant.grow(1)
                        print(f"Watered {plant.get_name()}, It is growing !")
                    else:
                        raise WaterError("Not enough water"
                                         " left to water the plants")
                if count == 0:
                    raise PlantError(plant.get_name())
        except GardenError as e:
            print(f"An error occured while watering : {e.message}")
        finally:
            print("close Watering system")

    def get_info(self):
        print(f"===== Welcome to {self.__name} Garden =====")
        print(f"{self.__name} Garden has {self.get_nb_of_plants()} plants")
        for plant in self.__list_of_plants:
            plant.get_info()
        print("===== Please come visit again ! =====")


def test_garden_management():
    print("Creating a garden :")
    rose = Plant("Rose", 3, 3)
    platane = Plant("Platane", 4, 4)
    empty_name = Plant("", 1, 1)
    garden = GardenManager("Mon Beau jardin", [rose, platane])

    print("\n== Success paths ==")
    rose.check_plant_health(5, 6)
    garden.water_plants()
    garden.get_info()

    try:
        empty_name.check_plant_health(5, 6)
    except ValueError as exc:
        print(f"check_plant_health name error: {exc}")

    try:
        rose.check_plant_health(0, 6)
    except ValueError as exc:
        print(f"check_plant_health water error: {exc}")

    try:
        rose.check_plant_health(5, 1)
    except ValueError as exc:
        print(f"check_plant_health sun error: {exc}")

    try:
        rose.get_garden()
    except GardenError as exc:
        print(f"get_garden error: {exc.message}")

    print("\n== Garden manager errors ==")
    try:
        garden.add_plants([rose])
    except GardenError as exc:
        print(f"add_plants error: {exc.message}")

    new_plant = Plant("Lily", 2, 2)
    try:
        garden.add_plants([new_plant])
        print("add_plants success: Lily added")
    except Exception as exc:
        print(f"add_plants unexpected error: {exc}")

    garden.watertank = 0
    try:
        garden.water_plants()
    except WaterError as exc:
        print(f"water_plants error: {exc}")

    print("\n== water_plant WaterError ==")
    garden.watertank = 10
    garden.water_plant("Rose")

    print("\n== water_plant PlantError ==")
    garden.watertank = 100
    garden.water_plant("Rose")


test_garden_management()
