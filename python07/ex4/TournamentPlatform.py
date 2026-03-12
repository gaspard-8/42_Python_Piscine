from ex4.TournamentCard import TournamentCard


class TournamentPlatform():
    cards: dict[str, TournamentCard] = {}
    nb_match = 0
    status = "active"

    def register_card(self, card: TournamentCard) -> str:
        self.cards.update({card.id: card})
        return f"card {card.name} ({card.id}) added to the platform"

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        self.nb_match += 1
        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]
        while card1.health > 0 and card2.health > 0:
            card1.attack(card2)
            if card2.health < 0:
                card1.update_wins(1)
                card2.update_losses(1)
                return {"winner": card1_id, "loser": card2_id, "winner_rating":
                        card1.calculate_rating(),
                        "loser rating": card2.calculate_rating()}
            card2.attack(card1)
            if card1.health < 0:
                card2.update_wins(1)
                card1.update_losses(1)
                return {"winner": card2_id, "loser": card1_id, "winner_rating":
                        card2.calculate_rating(),
                        "loser rating": card1.calculate_rating()}
        raise ValueError("Shouldnt happen")

    def get_leaderboard(self) -> list:
        lst = self.cards.items()
        temp = sorted(lst, key=lambda obj: (- obj[1].calculate_rating()))
        return [a[0] for a in temp]

    def generate_tournament_report(self) -> dict:
        lst = self.cards.items()
        avg_rating = sum([card[1].calculate_rating() for card in lst])/len(lst)
        return {"total_cards": len(lst), "matches_played": self.nb_match,
                "avg_rating": avg_rating, "platform_status": self.status}
