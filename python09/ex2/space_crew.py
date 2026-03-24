from pydantic import BaseModel, Field, model_validator, ValidationError
from enum import Enum
from datetime import datetime
from space_missions import SPACE_MISSIONS


class Rank(Enum):
    RCADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: list[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def check(self):
        if self.mission_id[0] != 'M':
            raise ValueError("Mission ID must start with 'M'")
        if not (Rank.COMMANDER in [member.rank for member in self.crew] and
                Rank.CAPTAIN in [member.rank for member in self.crew]):
            raise ValueError("Mission requires a commander and a captain")
        if (self.duration_days > 365):
            exp_members = []
            for member in self.crew:
                if member.years_experience >= 5:
                    exp_members.append(member)
            if len(exp_members) < len(self.crew)/2:
                raise ValueError("Crew members lack experience")
        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active for the mission")
        return self

    def display(self) -> None:
        print("Valid mission created:")
        print(f"Mission: {self.mission_name}")
        print(f"ID: {self.mission_id}")
        print(f"Destination: {self.destination}")
        print(f"Duration: {self.duration_days} days")
        print(f"Budget: ${self.budget_millions:.2f}M")
        print(f"Crew size: {len(self.crew)}")
        print("Crew members:")
        for member in self.crew:
            print(f"- {member.name} - {member.specialization}")
        print()


def main():

    print("Spacee Mission Crew validation")
    print("===========================================")
    print("Testing valid space missions")
    for mission in SPACE_MISSIONS:
        try:
            miss = SpaceMission(**mission)
            miss.display()
        except ValidationError as e:
            print(e.errors()[0]["msg"] + " | Aborting mission")
            print()


if __name__ == "__main__":
    main()
