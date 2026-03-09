from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArticfactCard import ArtifactCard
from ex1.Spellcard import SpellCard
import random


class Deck:
    cards_list: list[Card] = []
    creature_cards = []
    spell_cards = []
    artifact_cards = []

    def add_cards(self, card: Card) -> None:
        if (isinstance(card, CreatureCard)):
            self.creature_cards.append(card)
        if (isinstance(card, SpellCard)):
            self.spell_cards.append(card)
        if (isinstance(card, ArtifactCard)):
            self.artifact_cards.append(card)
        self.cards_list.append(card)

    def remove_card(self, card_name: str) -> bool:
        i = 0
        for card in self.cards_list:
            if card.name == card_name:
                self.cards_list.pop(i)
                return True
            i += 1
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards_list)

    def draw_card(self) -> Card:
        card = self.cards_list[0]
        self.cards_list.pop(0)
        return card

    def get_deck_stats(self) -> dict:
        nb_crea = len(self.creature_cards)
        nb_spells = len(self.spell_cards)
        nb_art = len(self.artifact_cards)
        mana = 0
        for card in self.cards_list:
            mana += card.cost
        avg = mana / len(self.cards_list)
        return {"total_cards": len(self.cards_list), "creatures": nb_crea,
                "spells": nb_spells, "artifacts": nb_art, "avg_cost": avg}
