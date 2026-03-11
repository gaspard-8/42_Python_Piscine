from ex3.AgressiveStrategy import AgressiveStrategy
from tools.card_generator import CardGenerator
from ex0.CreatureCard import CreatureCard
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameEngine import GameEngine


def main():
    card_gen = CardGenerator()
    card0 = CreatureCard(**card_gen.get_random_creature())
    card1 = CreatureCard(**card_gen.get_random_creature())
    card2 = CreatureCard(**card_gen.get_random_creature())
    target0 = CreatureCard(**card_gen.get_random_creature())
    print(card0.name, card1.name, card2.name)
    hand = [card0, card1, card2]
    battlefield = [target0]
    print()

    print("=== Datadeck Game Engine ===")
    print()
    print("Configuring Fantasy Card Game...")
    strat = AgressiveStrategy()
    print()

    print("simulating agressive turn...")
    print("Hand:", end=" ")
    print([f"{card.name} ({card.cost})" for card in hand])
    print()

    print("Turn execution: ")
    print(strat.execute_turn(hand, battlefield))
    print()

    print("===Testing deck generator===")
    card_fact = FantasyCardFactory()
    deck = card_fact.create_themed_deck(25)
    print(deck.get_deck_stats())
    print(deck.draw_card().name)

    print("Testing Game engine")
    engine = GameEngine()
    engine.configure_engine(card_fact, strat)
    print("Configuring engine ... ")
    print("Game report: ")
    engine.simulate_turn()
    engine.simulate_turn()
    print(f"GameEngine report : {engine.get_engine_status()}")


if __name__ == "__main__":
    main()
