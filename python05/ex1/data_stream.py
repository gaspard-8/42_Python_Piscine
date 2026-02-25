#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, Optional, Union, Dict


class DataStream(ABC):

    def __init__(self, stream_id: str) -> None:
        super().__init__()
        self.id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: list[Any]) -> str:
        pass

    def filter_data(self, data_batch: list[Any],
                    criteria: Optional[str] = None) -> list[Any]:
        list = []
        for data in data_batch:
            if (data != criteria):
                list.append(data)
        return list


        pass

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        pass
    @abstractmethod


class Sensorstream(DataStream):
    pass


class TransactionStream(DataStream):
    pass


class EventStream(DataStream):
    pass
