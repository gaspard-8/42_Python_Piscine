#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Protocol, Any


class ProcessingStage(Protocol):

    def process(self, data: Any) -> Any: ...


class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: str):
        self.id = pipeline_id
        self.stages: list[ProcessingStage] = []

    def add_stage(self, stage: ProcessingStage):
        self.stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> Any: ...


class JSONAdapter(ProcessingPipeline):

    def process(self, data: Any) -> Any:
        input = self.stages[0].process(data)
        input.update({"type": "JSON"})
        trans = self.stages[1].process(input)
        output = self.stages[2].process(trans)
        return output


class CSVAdapter(ProcessingPipeline):

    def process(self, data: Any) -> Any:
        data = data.split(',')
        if not len(data) % 3 == 0:
            raise ValueError("Error before processing : data is not valid")
        dic = {"user": [], "action": [], "timestamp": []}
        for i in range(len(data) // 3):
            dic["user"].append(data[i])
            dic["action"].append(data[i+1])
            dic["timestamp"].append(data[i+2])
        input = self.stages[0].process(dic)
        input.update({"type": "CSV"})
        trans = self.stages[1].process(input)
        output = self.stages[2].process(trans)
        return output


class StreamAdapter(ProcessingPipeline):

    def process(self, data: Any) -> Any:
        data = data.split(",")
        try:
            dic = {"type_of_data": data[0], "readings": [float(thing) for
                                                         thing in data[1:]]}
        except Exception:
            raise ValueError("Error before processing, data invalid")
        input = self.stages[0].process(dic)
        input.update({"type": "Stream"})
        trans = self.stages[1].process(input)
        output = self.stages[2].process(trans)
        return output


class InputStage():
    def process(self, data: Any) -> dict:
        if isinstance(data, dict):
            return data
        else:
            try:
                data_0 = dict(data)
                return data_0
            except Exception:
                raise ValueError(f"Error at stage 1: {data} is not a valid "
                                 f"dictionnary")


class TransformStage():
    def process(self, data: dict) -> dict:
        if data["type"] == "JSON":
            if data["value"] > -10 and data["value"] < 40:
                data.update({"status": "Normal range"})
            else:
                data.update({"status": "Abnormal range"})
        if data["type"] == "CSV":
            data.update({"action_nb": len(data["action"])})
        if data["type"] == "Stream":
            for reading in data["readings"]:
                data.update({"nb_of_readings": len(data["readings"])})
                data.update({"avg": sum(data["readings"])
                             / len(data["readings"])})
        return data


class OutputStage:
    def process(self, data: dict) -> str:
        if data["type"] == "JSON":
            return (f"Processed temperature reading: {data['value']}"
                    f"°{data['unit']}({data['status']})")
        if data["type"] == "CSV":
            return (f"User activity logged : {data['action_nb']}"
                    f" action(s) processed")
        if data["type"] == "Stream":
            return (f"Stream summary: {data['nb_of_readings']} readings of "
                    f"{data['type_of_data']},"
                    f" avg: {data['avg']}")
        else:
            raise ValueError("Error in stage 3: Weird")


class NexusManager():
    pipelines: dict[str, ProcessingPipeline] = {}
    capacity = 1000

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.update({pipeline.id: pipeline})

    def process_data(self, data: Any, id: str = "chained") -> Any:
        if id != "chained":
            try:
                data = self.pipelines[id].process(data)
            except KeyError:
                raise ValueError(f"{id} is not a valid pipeline id")
        else:
            for pipeline in self.pipelines.items():
                data = pipeline[1].process(data)
        return data


def main() -> None:
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===")
    print()
    print("Intitializing Nexus Manager...")
    manager = NexusManager()
    print(f"Pipeline capacity: {manager.capacity}")
    print("Creating Data Processing Pipeline...")
    manager.add_pipeline(JSONAdapter("JSON_00"))
    manager.add_pipeline(CSVAdapter("CSV_00"))
    manager.add_pipeline(StreamAdapter("STREAM_00"))
    for pipeline in manager.pipelines.items():
        pipeline[1].add_stage(InputStage())
        pipeline[1].add_stage(TransformStage())
        pipeline[1].add_stage(OutputStage())
    print()
    print("Multi-format Data Processing ===")
    print("Processing JSON data through pipeline...")
    print()
    input = {"sensor": "temp", "value": 23.5, "unit": "C"}

    JSON_data = manager.process_data(input, "JSON_00")
    print(JSON_data)

    print()
    print()
    print("processing CSV data through the same pipeline...")
    input = "Gaspard,salut,maintenant,Gil,Hey,now"
    print(f"Input: {input}")
    CSV_data = manager.process_data(input, "CSV_00")
    print(CSV_data)
    print()

    print("Processing Stream data through sams pipeline...")
    input = "temp,22.5,23,20,18,13.5,32"
    print(f"Input: {input}")
    Stream_data = manager.process_data(input, "STREAM_00")
    print(Stream_data)
    print()

    print("Testing invalid data")
    input = "temp,22.5,23,Salut,13.5,32"
    print(f"Input: {input}")
    try:
        Stream_data = manager.process_data(input, "STREAM_00")
        print(Stream_data)
    except ValueError as e:
        print(e)

    print()
    try:
        print("processing CSV data through the same pipeline...")
        input = "Gaspard,salut,Gil,Hey,now"
        print(f"Input: {input}")
        CSV_data = manager.process_data(input, "CSV_00")
        print(CSV_data)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
