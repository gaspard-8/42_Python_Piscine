from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int):
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        playable = self.is_playable(game_state["available_mana"])
        if playable:
            return {"card_played": self.name, "mana_used": self.cost,
                    "effects": "Creature summoned to battlefield"}
        else:
            return {"card_played": self.name, "mana_used": 0,
                    "effect": "summoning failed"}

    def attack_target(self, target) -> dict:
        if (self.health > 0 and self.attack > 0):
            return {"attacker": self.name, "target": target.name,
                    "damage_dealt": self.attack, "combat_resolved": True}
        else:
            return {"attacker": self.name, "target": target.name,
                    "damage_dealt": 0, "combat_resolved": False}

    def get_card_info(self) -> dict:
        dict = super().get_card_info()
        dict.update({"type": "Creature", "attack": self.attack,
                     "health": self.health})
        return dict

# update({"type": "Creature",
#                                  "attack": self.attack,
#                                   "health": self.health}))
