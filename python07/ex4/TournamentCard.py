
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, armor: int, health: int, id: str):
        super().__init__(name, cost, rarity)
        self.atk = attack
        self.armor = armor
        self.wins = 0
        self.losses = 0
        self.id = id
        self.health = health

    def play(self, game_state: dict) -> dict:
        playable = self.is_playable(game_state["available_mana"])
        if playable:
            return {"card_played": self.name, "mana_used": self.cost}
        else:
            raise ValueError("not enough mana")

    def attack(self, target) -> dict:
        target.health -= self.atk
        result = {"attacker": {self.name}, "target": target.name}
        return result

    def defend(self, incoming_damage: int) -> dict:
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

    def get_combat_stats(self) -> dict:
        return {"attack": self.atk, "armor": self.armor,
                "health": self.health}

    def calculate_rating(self) -> int:
        return 1000 + (self.wins * 20) - (self.losses * 20)

    def update_wins(self, wins: int) -> None:
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses

    def get_rank_info(self) -> dict:
        return {"rating": self.calculate_rating(),
                "wins": self.wins, "losses": self.losses}
