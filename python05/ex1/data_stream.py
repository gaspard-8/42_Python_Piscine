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
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"stream_id": self.id}


class Sensorstream(DataStream):
    def __init__(self, stream_id: str, type: str) -> None:
        super().__init__(stream_id)
        self.type = type
        self.readings = 0
        self.temp: list[float] = []
        self.humidity: list[float] = []
        self.pressure: list[int] = []

    def process_batch(self, data_batch: list[str]) -> str:
        for data in data_batch:
            key = data.split(":")
            self.readings += 1
            match key[0]:
                case "temp":
                    self.temp.append(float(key[1]))
                case "humidity":
                    self.humidity.append(float(key[1]))
                case "pressure":
                    self.pressure.append(int(key[1]))
                case _:
                    self.readings += -1
                    raise ValueError(f"{data} is not a valid measure")

        return f"processed sensor barch : {data_batch}"

    def filter_data(self, data_batch: list[str],
                    criteria: str | None = None) -> list[str]:
        new_data = []
        for data in data_batch:
            if criteria == data.split(":")[0]:
                new_data.append(data)
        return (new_data)

    def get_stats(self) -> Dict[str, str | int | float]:
        if len(self.temp) == 0:
            avg_temp = ""
        else:
            avg_temp = sum(self.temp) / len(self.temp)
        if len(self.humidity) == 0:
            avg_humidity = ""
        else:
            avg_humidity = sum(self.humidity) / len(self.humidity)
        if len(self.pressure) == 0:
            avg_pressure = ""
        else:
            avg_pressure = sum(self.pressure) / len(self.pressure)
        return {"stream_id": self.id, "streams processed": self.readings,
                "avg_temp": avg_temp,
                "avg_humidity": avg_humidity, "avg_pressure": avg_pressure}


class TransactionStream(DataStream):
    def __init__(self, stream_id: str, type: str) -> None:
        super().__init__(stream_id)
        self.type = type
        self.readings = 0
        self.net = 0

    def process_batch(self, data_batch: list[str]) -> str:
        for data in data_batch:
            key = data.split(":")
            self.readings += 1
            match key[0]:
                case "buy":
                    self.net += int(key[1])
                case "sell":
                    self.net -= int(key[1])
                case _:
                    self.readings += -1
                    raise ValueError(f"{data} is not a valid transaction")

        return f"processed sensor barch : {data_batch}"

    def filter_data(self, data_batch: list[str],
                    criteria: str | None = None) -> list[str]:
        new_data = []
        if criteria != "high":
            return data_batch
        for data in data_batch:
            if int(data.split(":")[1]) > 100:
                new_data.append(data)
        return (new_data)

    def get_stats(self) -> Dict[str, str | int | float]:
        return {"stream_id": self.id, "streams processed": self.readings,
                "net units": self.net}


class EventStream(DataStream):
    def __init__(self, stream_id: str, type: str) -> None:
        super().__init__(stream_id)
        self.type = type
        self.readings = 0
        self.errors = 0
        self.usr_log = False

    def process_batch(self, data_batch: list[str]) -> str:
        for data in data_batch:
            self.readings += 1
            match data:
                case "login":
                    self.usr_log = True
                case "logout":
                    self.usr_log = False
                case _:
                    self.readings += -1
                    raise ValueError(f"{data} is not a valid log")

        return f"processed sensor barch : {data_batch}"

    def filter_data(self, data_batch: list[Any], criteria: str |
                    None = None) -> list[Any]:
        list = []
        if (criteria != "error"):
            return data_batch
        for data in data_batch:
            if data == criteria:
                list.append(data)
        return list


def main():

    print("Initializing Sensor stream with ID SENSOR_001 and type:"
          " 'Environmental data'")
    sens_stream = Sensorstream("SENSOR_001", "Environmental data")
    try:
        print(sens_stream.process_batch(["temp:432.4", "humidity:43",
                                        "pressure:1013"]))
    except Exception as e:
        print(e)
    print("processing filtered data : ...")
    try:
        sens_stream.process_batch(sens_stream.filter_data
                                  (["temp:400", "humidity:43",
                                    "pressure:1013"], "temp"))
    except Exception as e:
        print(e)
    print(f"Stats of the stream :{sens_stream.get_stats()}")
    print(f"{sens_stream.temp}{sens_stream.humidity}")

    print("Initializing Sensor stream with ID TRANS_001 and type:"
          " 'Financial data'")
    trans_stream = TransactionStream("SENSOR_001", "Environmental data")
    try:
        print(trans_stream.process_batch(["buy:100", "sell:150", "buy:75"]))
    except Exception as e:
        print(e)
    print("processing filtered data : ...")
    try:
        trans_stream.process_batch(trans_stream.filter_data
                                   (["buy:90", "sell:150", "buy:75"], "high"))
    except Exception as e:
        print(e)
    print(f"Stats of the stream :{trans_stream.get_stats()}")




if __name__ == "__main__":
    main()
