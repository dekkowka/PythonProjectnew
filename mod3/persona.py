import datetime
from typing import Optional

class Person:
    def __init__(self, name: str, year_of_birth: int, address: Optional[str] = None):  # Use Optional[str] and None
        self.name = name
        self.yob = year_of_birth
        self.address = address or ""

    def get_age(self) -> int:
        now = datetime.datetime.now()
        return now.year - self.yob

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    def set_address(self, address: str) -> None:
        self.address = address

    def get_address(self) -> str:
        return self.address

    def is_homeless(self) -> bool:
        return not self.address