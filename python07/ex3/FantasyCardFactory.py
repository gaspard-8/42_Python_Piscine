from ex0.Card import Card
from ex3.CardFactory import CardFactory
from random import randint, choice
from ex0.CreatureCard import CreatureCard
from ex1.Spellcard import SpellCard
from ex1.ArticfactCard import ArtifactCard
from ex1.Deck import Deck


class FantasyCardFactory(CardFactory):

    name = "FantasyCardFactory"
    crea_name = ["Kevin le gobelin", "Andre la moustache", "Kevin le troll",
                 "Jun la sorcière", "Mathieu la sirène"]
    spell_name = ["abracadabra", "pouf", "paf", "pif", "Vroum"]
    effects = ["transforme en grenouille", "transforme en canard",
               "rend chauve", "fait rien"]
    art_effects = ["il fait soleil", "il pleut", "il neige", "+1 mana"]
    artifact_name = ["pierre enchanté", "caillou magique", "rocher chelou"]
    rarities = ["Common", "Rare", "Epic", "Legendary"]

    def create_creature(self, name_or_power:
                        str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            name = name_or_power
            cost = randint(1, 7)
        elif isinstance(name_or_power, int):
            name = choice(self.crea_name)
            cost = name_or_power
        else:
            name = choice(self.crea_name)
            cost = randint(1, 7)
        return CreatureCard(name, cost,
                            choice(self.rarities),
                            randint(1, 5), randint(5, 20))

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            name = name_or_power
            cost = randint(1, 7)
        elif isinstance(name_or_power, int):
            name = choice(self.crea_name)
            cost = name_or_power
        else:
            name = choice(self.crea_name)
            cost = randint(1, 7)
        return SpellCard(name, cost,
                         choice(self.rarities), choice(self.effects))

    def create_artifact(self, name_or_power:

                        str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            name = name_or_power
            cost = randint(1, 7)
        elif isinstance(name_or_power, int):
            name = choice(self.crea_name)
            cost = name_or_power
        else:
            name = choice(self.crea_name)
            cost = randint(1, 7)
        return ArtifactCard(name, cost,
                            choice(self.rarities),
                            randint(1, 5), choice(self.art_effects))

    def create_themed_deck(self, size: int) -> Deck:
        deck = Deck()
        for i in range(size):
            j = randint(0, 5)
            if j in {0, 1, 2}:
                deck.add_cards(self.create_creature())
            if j in {3, 4}:
                deck.add_cards(self.create_spell())
            if j == 5:
                deck.add_cards(self.create_artifact())
        return deck

    def get_supported_types(self) -> dict:
        return {"creatures": (self.crea_name),
                "spells": (self.spell_name),
                "artifact": (self.artifact_name)}
