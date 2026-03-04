#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Protocol, Any


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any: ...


class ProcessingPipeline(ABC):
    stages: list[ProcessingStage]

    def add_stage(self, stage: ProcessingStage):
        self.stages.append(stage)

    @abstractmethod
    def process(data: Any) -> Any: ...


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str):
        self.id = pipeline_id

    def process(self, data: Any) -> Any:
        pass

def main():
    pass


if __name__ == "__main__":
    main()
