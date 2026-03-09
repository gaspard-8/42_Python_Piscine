from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        playable = self.is_playable(game_state["available_mana"])
        if playable:
            self.activate_ability()
            result = {"card_played": self.name, "mana_used": self.cost,
                      "effects": "Permanent: "+self.effect}
            return result
        else:
            raise ValueError("Errorrrerer")

    def activate_ability(self):
        print(self.effect)
