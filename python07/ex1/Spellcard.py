from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        self.discarded = False

    def play(self, game_state: dict) -> dict:
        playable = (self.is_playable(game_state["available_mana"])
                    and not self.discarded)
        if playable:
            eff = self.resolve_effect(game_state["targets"])
            result = {"card_played": self.name, "mana_used": self.cost,
                      "effects": eff["message"]}
            self.discarded = True
            return result
        else:
            return {"card_played": self.name, "mana_used": 0,
                    "effect": "spell failed"}

    def resolve_effect(self, targets: list) -> dict:
        match self.effect_type:
            case "damage":
                for target in targets:
                    target.health -= self.cost
                return {"message": f"Deal {self.cost} damage to target"}
            case "heal":
                for target in targets:
                    target.health += self.cost
                return {"message": f"Heal {self.cost} hp to target"}
            case "buff":
                for target in targets:
                    target.attack += self.cost
                return {"message": f"Buff {self.cost} Attack points to target"}
            case "buff":
                for target in targets:
                    target.attack -= self.cost
                return {"message": f"debuff {self.cost} attacks to target"}
            case _:
                raise ValueError("ErOoOrRrR")

    def __del__(self):
        del self
