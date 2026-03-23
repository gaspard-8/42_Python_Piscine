from ex0.CreatureCard import CreatureCard
from ex0.Card import Card
from ex2.EliteCard import EliteCard
from ex2.Combatable import Combatable
from ex2.Magical import Magical


def main():

    print("=== DataDekck Ability System ===")
    print()

    print("EliteCard capabilities:")
    print(f"Card: {dir(Card)[-3:]}")
    print(f"Combatable: {dir(Combatable)[-3:]}")
    print(f"Magical: {dir(Magical)[-3:]}")
    print()

    print("Playing Arcane Warrior (Elite Card):")
    print()

    target = CreatureCard("Enemy", 3, "Common", 3, 3)
    game = {"available_mana": 5}
    elite = EliteCard("Arcane Warrior", 5, "Legendary", 7, 3, 10, 5, "melee")
    print(f"play : {elite.play(game)}")

    print()
    print(f"Attack result: {elite.attack(target)}")
    print(f"Defense result: {elite.defend(5)}")

    print()
    print("Magic phase:")
    print(f"Spell cast: {elite.cast_spell('Fireball', [target.name])}")
    print(f"Mana channel: {elite.channel_mana(4)}")

    print()
    print("Multiple interface implementation successful!")


if __name__ == "__main__":
    main()
