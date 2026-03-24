from functools import wraps
from time import time, sleep
from typing import Any, Callable


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print(f"Casting {func.__name__}")
        start = time()
        a = func(*args, **kwargs)
        print(f"Spell completed in {time() - start:.2f} seconds")
        return a

    return wrapper


def power_validator(min_power: int) -> Callable:

    def power_decorator(func: Callable):

        @wraps(func)
        def validator(*args, **kwargs) -> Any:
            power = kwargs.get("power")
            if power is None:
                return "No power argument found"
            if (power >= min_power):
                return func(*args, **kwargs)
            else:
                return "Inusfficient power for this spell"

        return validator

    return power_decorator


def retry_spell(max_attempts: int) -> Callable:

    def retry_decorator(func: Callable):
        @wraps(func)
        def retry(*arg, **kwargs) -> Any:
            attempts = 0
            while attempts < max_attempts:
                try:
                    a = func(*arg, **kwargs)
                    return a
                except Exception:
                    attempts += 1
                    print(f"Spell failed, retrying... (attempt {attempts}/"
                          f"{max_attempts})")
            return "Spell failed"

        return retry

    return retry_decorator


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        if len(name) >= 3:
            for char in name:
                if not (char.isalpha() or char == ' '):
                    return False
        return True

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main():

    @spell_timer
    def sleeping_function() -> str:
        sleep(2)
        return "J'ai bien dormi"

    print(sleeping_function())

    @power_validator(10)
    def spell(power: int):
        return (f"BOOM {power} damage")

    print()
    print(f"Casting powerful spell (20 power) : {spell(20)}")
    print(f"Casting weak spell (5 power): {spell(5)}")
    print()

    @retry_spell(5)
    def bad_function() -> str:
        raise ValueError

    @retry_spell(3)
    def good_function() -> str:
        return ("I work well")

    print("Testing the retry  decorator with a working function:")
    print(f"good_function(): {good_function()}")
    print()
    print("Testing the retry decorator with a flawed function:")
    print(f"bad_function(): {bad_function()}")

    print()
    print()
    print("Testing the MageGuild class")
    print("testing the validate name method on invalid names")
    invalid_names = ['Jo', 'A', 'Alex123', 'Test@Name']
    for name in invalid_names:
        print(MageGuild.validate_mage_name(name))
    print()
    print("testing the validate name method on valid names")
    mage_names = ['Casey', 'Alex', 'Morgan', 'River', 'Storm', 'Kai']
    for name in mage_names:
        print(MageGuild.validate_mage_name(name))

    print()
    print("Casting spells ....")
    print(f"casting spell with 5 power : "
          f"{MageGuild().cast_spell('fireball',power = 5)}")
    print(f"casting spell with 20 power : "
          f"{MageGuild().cast_spell('fireball',power = 20)}")


if __name__ == "__main__":
    main()
