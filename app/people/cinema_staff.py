class Cleaner():
    def __init__(self, name: str) -> None:   # Name cleaner
        self.name = name

    def clean_hall(self, hall_number: int) -> None:
        print(f"Cleaner {self.name} is cleaning "
              f"hall number {hall_number}.")
