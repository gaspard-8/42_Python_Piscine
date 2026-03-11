from ex3.GameStrategy import GameStrategy
from ex0.CreatureCard import CreatureCard


class AgressiveStrategy(GameStrategy):

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        prio_targets = self.prioritize_targets(battlefield)
        game_state = {"available_mana": 8,
                      "targets": prio_targets}
        result = {"srategy": self.get_strategy_name(), "cards played": [],
                  "targets_attacked": [tar.name for tar in prio_targets],
                  "damage_dealt": 0}
        for card in hand:
            if isinstance(card, CreatureCard) and card.cost <= 3:
                try:
                    card.play(game_state)
                    game_state["available_mana"] -= card.cost
                    result["cards played"].append(card.name)
                    result["damage_dealt"] += card.attack
                except ValueError:
                    return result
        return result

    def get_strategy_name(self):
        return "AgressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        targets = sorted(available_targets, key=lambda obj: obj.health)
        return targets
