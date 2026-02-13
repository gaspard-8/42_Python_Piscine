class GardenError(Exception):
    message = "A garden related error occured"
    pass


class PlantError(GardenError):
    def __init__(self, plant: str):
        self.message = f"A {plant} related error occured"
    pass


class TypePlantError(GardenError):
    def __init__(self, type_: type):
        self.message = f"the elemt is a {type_} not a Plant"


class WaterError(GardenError):
    message = "Not enough water left to water the plants"
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
            raise GardenError
        else:
            return self.__garden

    def grow(self, size: int):
        self.__height = self.__height + size

    def age(self, days: int):
        self.__age = self.__age + days

    def get_info(self):
        print(f"{self.__name}: {self.__height}cm, {self.__age} days old")

    def score(self) -> int:
        return self.__height


class Garden:
    def __init__(self, name: str, plants: list[Plant]):
        self.__name = name
        self.__list_of_plants = plants
        self.watertank = 100

    def add_plants(self, plants: list[Plant]):
        for plant in plants:
            self.__list_of_plants.append(plant)
            plant.set_garden

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
        if self.get_nb_of_plants() * 10 < self.watertank:
            raise WaterError
        else:
            self.grow(1)

    def water_plant(self, plant_name: str):
        count = 0
        for plant in self.__list_of_plants:
            if plant.get_name() == plant_name:
                if self.watertank > 10:
                    plant.grow(1)
                else:
                    raise WaterError
            if count == 0:
                raise PlantError(plant.get_name())


def water_plants(plant_list: list[Plant]) -> int:
    check = 1
    try:
        for plant in plant_list:
            if plant.__class__ == Plant:
                print(f"Watered {plant.get_name()}")
            else:
                raise TypePlantError(type(plant))
    except TypePlantError as e:
        print(f"Watering Error : {e.message}")
        check = 0
    finally:
        print("closes the watering system")
        return check


def test_watering_system():
    list = []
    list.append(Plant("rose", 3, 3))
    list.append(Plant("BG", 4, 5))
    list.append(Plant("platane", 4, 4))
    print("")
    if water_plants(list):
        print("Watering completed successfully")
    print()
    list.append("Salut")
    if water_plants(list):
        print("Watering completed successfully")


test_watering_system()
