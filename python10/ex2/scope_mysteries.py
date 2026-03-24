from typing import Callable, Any


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable:
    power = initial_power

    def accumulate(more_power: int) -> int:
        nonlocal power
        power += more_power
        return power

    return accumulate


def enchantment_factory(enchantment_type: str) -> Callable:

    def enchant(item: str) -> str:
        return (f"{enchantment_type} {item}")

    return enchant


def memory_vault() -> dict[str, Callable]:
    memory: dict[str, Callable] = {}

    def store(key: str, value: Any) -> None:
        memory.update({key: value})

    def recall(key: str) -> Any | str:
        if key in memory.keys():
            return memory[key]
        else:
            return "Memory not found"

    return {"store": store, "recall": recall}


def main():
    print("Testing counter :")
    count = mage_counter()
    print("Counting ... : ")
    for i in range(10):
        print(count())
    print()
    print("Testing accumulating power (10 initial + 5 each time)")
    power = spell_accumulator(10)
    for i in range(10):
        print(f"Current power: {power(5)}")

    print()
    print("Testing enchantment_factory")
    print("Creating a fire enchantment")
    fire = enchantment_factory("Blazing")
    items = ['Wand', 'Amulet', 'Sword', 'Ring']
    for item in items:
        print(fire(item))
    print()
    print("Testing memory vault system")

    bibliotheque = memory_vault()
    bibliotheque["store"]("Livre", "les Misérables")
    bibliotheque["store"]("BD", "Asterix chez les goths")
    print("looking for book", end=":  ")
    print(bibliotheque["recall"]("Livre"))
    print(f"Looking for BD: {bibliotheque['recall']('BD')}")
    print(f"Looking for DVD: {bibliotheque['recall']('DVD')}")
    return


if __name__ == "__main__":
    main()
