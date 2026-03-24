from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional
import json


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = None

    def display(self) -> None:
        print(f"ID: {self.station_id}")
        print(f"Name: {self.name}")
        print(f"Crew: {self.crew_size} people")
        print(f"Power: {self.power_level}")
        print(f"Oxygen: {self.oxygen_level}")
        print(f"Status: {'operational' if self.is_operational else 'Down'}")
        print(f"notes : {self.notes}" if self.notes else "")


def main():
    print("Space Station Data Validation")

    print("==================================================================")
    space = SpaceStation(station_id="ISS001", name="Internation Soace Station",
                         crew_size=6, power_level=23.3, oxygen_level=21.3,
                         last_maintenance=datetime.now(), is_operational=True,
                         )
    space.display()
    print()
    print("Testing wiht incorrect input:")
    try:
        space = SpaceStation(station_id="ISS001", name="Internation  Station",
                             crew_size=76, power_level=23.3, oxygen_level=21.3,
                             last_maintenance=datetime.now(),
                             is_operational=True)
    except ValidationError as e:
        print(e.errors()[0]["msg"])
    print()

    print("Using the generators provided:")
    file_name = "../generated_data/space_stations.json"
    try:
        with open(file_name) as f:
            data = json.load(f)
    except Exception as e:
        print(e)
        return
    for station in data:
        space = SpaceStation(**station)
        print()
        space.display()


if __name__ == "__main__":
    main()
