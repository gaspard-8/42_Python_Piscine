#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise TypeError(f"Error detected:, the following data is"
                            f" not numerical :{data} ")
        if data is int:
            data = [data]
        sum = 0
        for number in data:
            sum += number
        return (f"Processed {len(data)} numeric values, sum ={sum}, "
                f"avg ={sum/len(data):.2f}")

    def validate(self, data: Any) -> bool:
        if (isinstance(data, int)):
            return True
        if (isinstance(data, list)):
            if all(isinstance(num, int) for num in data):
                return True
        return False


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise TypeError(f"Error detected: the following data is"
                            f" not text:{data} ")
        return (f"Processed text: {len(data)} characters,"
                f" {len(data.split())} words")

    def validate(self, data: Any) -> bool:
        if (isinstance(data, str)):
            return True
        return False


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise TypeError(f"Error detected: the following data is"
                            f" not text:{data} ")
        log = data.split()
        return (f"{log[0]} level detected :"
                f" {' '.join(log[1:])}")

    def validate(self, data: Any) -> bool:
        if (isinstance(data, str)):
            return True
        return False

    def format_output(self, result: str) -> str:
        return f"[{result.split()[0]}] {result}"


def main():
    data1 = [1, 2, "aah", 4, 5]
    data2 = "Hello Nexus World"
    data3 = "ERROR Connection timeout"
    print("=== CODE NEXUS _ DATA PROCESSOR FOUNDATION ===")
    print()
    print("Initializing Numeric Procesesor...")
    print(f"Processing data : {data1}")
    NumericProcessor().validate(data1)
    try:
        print(NumericProcessor().format_output(NumericProcessor().
                                               process(data1)))
    except TypeError as e:
        print(e)
    print("Initializing Text Procesesor...")
    print(f"Processing data : {data2}")
    TextProcessor().validate(data2)
    try:
        print(TextProcessor().format_output(TextProcessor().process(data3)))
    except TypeError as e:
        print(e)

    print("Initializing Log Procesesor...")
    print(f"Processing data : {data3}")
    TextProcessor().validate(data3)
    try:
        print(LogProcessor().format_output(LogProcessor().process(data3)))
    except TypeError as e:
        print(e)

    print()
    print("==== Polymorphic processing Demo ===")
    cls = [NumericProcessor, TextProcessor, LogProcessor]
    data = [data1, data2, data3]
    for i in range(3):
        try:
            print(f"Result {i + 1}: {cls[i]().process(data[i])}")
        except TypeError as e:
            print(e)
    return


if __name__ == "__main__":
    main()
