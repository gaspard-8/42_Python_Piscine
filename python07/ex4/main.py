from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main():
    print("=== DataDeck tournament Platform ===")
    print()

    print("Register tournament card")
    card = TournamentCard("Fire dragon", 4, "Rare", 7, 7, 2, "dragon_001")
    print("Fire dragon (ID: dragon_001):")
    print("Interfaces: [Card, Combatable, Rankable]")
    print(f"Rating: {card.calculate_rating()}")
    print(f"Record {card.wins}-{card.losses}")
    print()

    card2 = TournamentCard("Ice wizard", 2, "Rare", 4, 7, 8, "wizard_001")
    print("Ice wizard (ID: wizard_001):")
    print("Interfaces: [Card, Combatable, Rankable]")
    print(f"Rating: {card2.calculate_rating()}")
    print(f"Record {card2.wins}-{card2.losses}")

    print()
    print("Creating tournament match...")
    print()

    tournament = TournamentPlatform()
    print(tournament.register_card(card))
    print(tournament.register_card(card2))
    print(tournament.create_match(card.id, card2.id))

    print("Second match:")
    print()

    print("Leaderboard:")
    for card_id in tournament.get_leaderboard():
        card = tournament.cards[card_id]
        print(f"{card.name} - Rating: {card.calculate_rating()} "
              f"({card.wins} - {card.losses})")

    print()
    print(f"Report: {tournament.generate_tournament_report()}")
    print("")
    pass


if __name__ == "__main__":
    main()
