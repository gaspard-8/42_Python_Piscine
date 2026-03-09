from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):

    def __init__(self, name: str, cost: int, rarity: str, atk: int, arm: int,
                 health: int, mana: int, type: str):
        super().__init__(name, cost, rarity)
        self.atk = atk
        self.armor = arm
        self.type = type
        self.health = health
        self.mana = mana

    def play(self, game_state: dict) -> dict:
        playable = self.is_playable(game_state["available_mana"])
        if playable:
            return {"card_played": self.name, "card_type": self.type,
                    "mana_used": self.cost}
        else:
            raise ValueError("card not playable")

    def attack(self, target) -> dict:
        target.health -= self.atk
        result = {"attacker": {self.name}, "target": target.name,
                  "combat_type": self.type}
        return result

    def defend(self, incoming_damage: int):
        dmg = (incoming_damage - self.armor)
        if dmg > 0:
            self.health -= dmg
            block = self.armor
        else:
            block = incoming_damage
            dmg = 0

        if self.health < 0:
            self.health = 0
        result = {"defender": self.name, "damage_taken": dmg,
                  "damage_blocked": block, "still alive": (self.health > 0)}
        return result

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        if self.mana >= 4:
            self.mana -= 4
            return {"caster": self.name, "spell": spell_name,
                    "targets": targets, "mana_used": 4}
        else:
            raise ValueError("Insufficient mana")

    def channel_mana(self, amount: int) -> dict:
        self.mana += amount
        return {"Channeled": amount, "total_mana": self.mana}

    def get_combat_stats(self) -> dict:
        return {"attack": self.atk, "armor": self.armor,
                "health": self.health, "type": self.type}

    def get_magic_stats(self) -> dict:
        return {"mana": self.mana, "type": self.type}
