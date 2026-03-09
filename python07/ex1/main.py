from ex1.Spellcard import SpellCard
from ex0.CreatureCard import CreatureCard
from ex1.ArticfactCard import ArtifactCard
from ex1.Deck import Deck


def main():
    print("=== DataDeck  Deck Builder ===")
    print()

    print("Building deck with different card types...")
    card = CreatureCard("Fire dragon", 5, "Legendary", 7, 5)
    spell = SpellCard("Lightning Bolt", 3, "Rare", "damage")
    artifact = ArtifactCard("Mana Crystal", 2, "Rare", 100, "+1 mana per turn")
    deck = Deck()
    deck.add_cards(card)
    deck.add_cards(spell)
    deck.add_cards(artifact)
    print(deck.get_deck_stats())

    print()
    print("Drawing and playing cards:")
    print()

    card = CreatureCard("Kevin", 5, "Legendary", 3, 3)
    card0 = deck.draw_card()
    print(f"Drew {card0.name}")
    print(card0.play({"targets": [card], "available_mana": 5}))

    print()
    card1 = deck.draw_card()
    print(f"Drew {card1.name}")
    print(card1.play({"targets": [card], "available_mana": 5}))

    print()
    card2 = deck.draw_card()
    print(f"Drew {card2.name}")
    print(card2.play({"targets": [card], "available_mana": 5}))

    print()
    print("Polymorphism in action: same interface, different card behavior")


if __name__ == "__main__":
    main()
