class SecurePlant:
    def __init__(self, Name: str, Height: int, Age: int):
        self.Name = Name
        self.Height = Height
        self.Age = Age
        pass

    def set_height(self, height=0) -> bool:
        if height < 0:
            print(f"Invalid set_height attempted : height={height} [REJECTED]")
            return (False)
        else:
            self.Height = height
            return (True)

    def set_age(self, age=0) -> bool:
        if age < 0:
            print(f"Invalid set_age attempted : age = {age} [REJECTED]")
            return (False)
        else:
            self.Age = age
        return (True)

    def get_height(self):
        if self.Height < 0:
            print("Security : Negative height rejected")
        else:
            print(f"Height of {self}: {self.Height}")

    def get_age(self):
        if self.Age < 0:
            print("Security : Negative age rejected")
        else:
            print(f"Age of {self}: {self.Age}")

    def get_info(self):
        print(f"{self.Name}: {self.Height}cm, {self.Age} days old")

def main():
    plant = SecurePlant(name)
    print(f"Created: {name} ({height}cm, {age} days)")
    plant.set_height25
