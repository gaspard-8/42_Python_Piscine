from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:

    def combine(*args):
        spell1(*args)
        spell2(*args)

    return combine


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:

    def new_spell(*args):
        return base_spell(*args) * multiplier

    return new_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:

    def conditional_spell(*args):
        if condition(*args):
            spell(*args)
        else:
            return "Spell fizzled"

    return conditional_spell


def spell_sequence(spells: list[Callable]) -> Callable:

    def sequence(*args):
        for spell in spells:
            spell(*args)

    return sequence


def main():
    def fireball(target: str, dmg: int) -> None:
        print(f"Fireball hits {target} for {dmg} damage")

    def heal(target: str, hp: int) -> None:
        print(f"Heals {target} for {hp}hp")

    def base_spell(dmg: int):
        return dmg + 10
    combiner = spell_combiner(fireball, heal)
    combiner("Dragon", 11)
    combiner("Goblin", 24)
    print()
    print("testing power amplifier (x10):")
    amplifier = power_amplifier(base_spell, 10)
    print(f"amplified power :{amplifier(11)}")
    print(f"amplified power :{amplifier(24)}")

    def condition(target: str, dmg: int):
        if dmg > 10 or target == "Dragon":
            return False
        return True
    print()
    print("Testing conditional spells")
    cond = conditional_caster(condition, fireball)
    print(cond("Dragon", 5))
    cond("Gobelin", 3)

    def iceball(target: str, dmg: int) -> None:
        print(f"iceeball hits {target} for {dmg} damage")

    def ligthningball(target: str, dmg: int) -> None:
        print(f"lightningball hits {target} for {dmg} damage")

    sequ = spell_sequence([fireball, heal, ligthningball, iceball])
    print("Testing sequence spells: ")
    sequ("Dragon", 42)

    return


if __name__ == "__main__":
    main()
