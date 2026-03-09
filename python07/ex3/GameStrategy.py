from abc import ABC, abstractmethod


class GameStrategy(ABC):

    @abstractmethod
    def execute_turn(self, hand: list, battlefield: list): ...
    @abstractmethod
    def get_strategy_name(self): ...
    @abstractmethod
    def prioritize_targets(self, available_targets: list): ...
