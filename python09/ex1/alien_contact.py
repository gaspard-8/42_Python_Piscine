from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from typing import Optional
from enum import Enum
import csv
import json


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: Optional[str] = None
    is_verified: bool = False

    @model_validator(mode='after')
    def check(self):
        if self.contact_id[0] != 'A' or self.contact_id[1] != 'C':
            raise ValueError(f"invalid id : {self.contact_id},"
                             f" id must start with: AC")
        if (self.contact_type == ContactType.PHYSICAL and
                not self.is_verified):
            raise ValueError("Physical contact requires verification")
        if (self.contact_type == ContactType.TELEPATHIC and
                self.witness_count < 3):
            raise ValueError("Telepathic contact report requires at "
                             "least 3 witnesses")
        if (self.signal_strength > 7.0 and self.message_received is None):
            raise ValueError(f"Strong signal ({self.signal_strength}) "
                             f"requires a message")
        return self

    def display(self) -> None:
        print("Valid contact report:")
        print(f"ID: {self.contact_id}")
        print(f"timestamp: {self.timestamp.date()}")
        print(f"Type: {self.contact_type.name}")
        print(f"Location: {self.location}")
        print(f"Signal: {self.signal_strength}")
        print(f"Duration: {self.duration_minutes} minutes")
        print(f"Witnesses: {self.witness_count}")
        print(f"Message : '{self.message_received}'" if self.message_received
              else None)


def main():
    print("Generating Contact reoprts from the generator")
    filename_valid = "../generated_data/alien_contacts.csv"
    filename_invalid = "../generated_data/invalid_contacts.json"
    with open(filename_valid) as f:
        valid_contact = list(csv.DictReader(f))
    with open(filename_invalid) as f:
        invalid_contact = json.load(f)
    for contact in valid_contact:
        temp = AlienContact(**contact)  # type: ignore
        temp.display()
        print()

    print("==========================================================")
    print()
    print("Testing invalid contact attempts: ")
    print()
    for contact in invalid_contact:
        try:
            temp = AlienContact(**contact)
            temp.display()
        except ValidationError as e:
            print(e.errors()[0]["msg"])
        print()
    pass


if __name__ == "__main__":
    main()
