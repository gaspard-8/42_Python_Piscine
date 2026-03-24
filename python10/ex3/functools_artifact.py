from typing import Callable
from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
import time


def spell_reducer(spells: list[int], operation: str) -> int:
    if operation == "add":
        return reduce(lambda x, y: add(x, y), spells)
    if operation == "multiply":
        return reduce(lambda x, y: mul(x, y), spells)
    if operation == "max":
        return reduce(lambda x, y: max(x, y), spells)
    if operation == "min":
        return reduce(lambda x, y: min(x, y), spells)
    else:
        raise ValueError("operation must be 'max, 'min', 'add' or 'multiply'")


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:

    return {"fire_enchant": partial(base_enchantment, 50, "fire"),
            "ice_enchant": partial(base_enchantment, 50, "ice"),
            "lightning_enchant": partial(base_enchantment, 50, "lightning")}


@lru_cache(maxsize=125)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable:
    @singledispatch
    def fun(s):
        print("Unspecified type, please enter an int, str or list")

    @fun.register(int)
    def _1(s: int):
        print(f"Dealing {s} dmg")

    @fun.register(str)
    def _2(s: str):
        print(f"Enchanting : {s}")

    @fun.register(list)
    def _3(s: list):
        for i in s:
            fun(i)

    return (fun)


def main():
    spells = [3, 2, 5, -3, 2, 43, 24, 7, -5]
    print(f"Testing reduce with spells = {spells}")
    print(f"add : {spell_reducer(spells, 'add')}")
    print(f"multiply: {spell_reducer(spells, 'multiply')}")
    print(f"max: {spell_reducer(spells, 'max')}")
    print(f"min: {spell_reducer(spells, 'min')}")
    try:
        print("Trying invalid operation : ", end="")
        print(f"Error: {spell_reducer(spells, 'Error')}")
    except ValueError as e:
        print(e)

    print()
    print("Testing partial functions")

    def enchant(power: int, element: "str", target: "str"):
        return f"Enchanted {target} with {element} element (+{power} power)"
    enchanter = partial_enchanter(enchant)
    print(f"fire enchant on a sword: {enchanter['fire_enchant']('Sword')}")
    print(f"ice enchant on a wand: {enchanter['ice_enchant']('Wand')}")
    print(f"lightning enchant on a talisman: "
          f"{enchanter['lightning_enchant']('Talisman')}")
    print()

    def bad_fibo(n: int) -> int:
        if n < 2:
            return n
        return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)

    print("Time taken with basic fibonacci (400):", end=" ")
    start = time.time()
    bad_fibo(400)
    print(time.time() - start)

    print("Time taken with lru_cache fibonacci (400), first try:")
    start = time.time()
    memoized_fibonacci(400)
    print(time.time() - start)

    print("Time taken with lru_cache fibonacci (400), second try:")
    start = time.time()
    memoized_fibonacci(400)
    print(time.time() - start)

    print()
    print("Testing spell_dispatcher")
    dis = spell_dispatcher()

    dis(3)
    dis("salut")
    dis(["Abracadabra", 4, "Okay", {4}])


if __name__ == "__main__":
    main()
