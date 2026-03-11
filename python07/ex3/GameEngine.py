from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine():
    factory: CardFactory
    strategy: GameStrategy
    turns_simulated = []

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        deck = self.factory.create_themed_deck(5)
        hand = [deck.draw_card() for i in range(5)]
        battlefield = [self.factory.create_creature() for i in range(3)]
        result = self.strategy.execute_turn(hand, battlefield)
        self.turns_simulated.append(result)
        return result

    def get_engine_status(self) -> dict:
        return {
                "supported_types": self.factory.get_supported_types(),
                "strategy chosen": self.strategy.get_strategy_name(),
                "simulated_turns": len(self.turns_simulated),
                "total_damage": sum([turn["damage_dealt"]
                                     for turn in self.turns_simulated])}
