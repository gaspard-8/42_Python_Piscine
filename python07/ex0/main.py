from ex0.CreatureCard import CreatureCard


def main():
    print("=== DataDeck Card Foundation ===")
    print()

    print("Testing Abstract Base Class Design:")
    print()

    card = CreatureCard("Fire dragon", 5, "Legendary", 7, 5)
    print("CreatureCard Info:")
    print(card.get_card_info())
    print()

    print("Playing Fire dragon with 6 mana available:")
    game_state = {"available_mana": 6}
    print(f"Playable: {card.is_playable(6)}")
    print(f"Play result: {card.play(game_state)}")

    print()
    card2 = CreatureCard("Goblin Warrior", 1, "Common", 3, 3)
    print(f"Attack result: {card.attack_target(card2)}")

    print()
    print("Testing insufficient mana (3 available)")
    print(f"Playable: {card.is_playable(3)}")


if __name__ == "__main__":
    main()
