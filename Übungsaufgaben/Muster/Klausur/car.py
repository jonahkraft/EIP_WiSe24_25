from __future__ import annotations
from datetime import date
from typing import List


class Car:
    def __init__(self, brand: str, model: str, year: int):
        self.brand: str = brand
        self.model: str = model
        self.year: int = year

    def get_brand(self) -> str:
        return self.brand

    def get_model(self) -> str:
        return self.model

    def get_year(self) -> int:
        return self.year

    def set_brand(self, brand: str) -> None:
        self.brand = brand

    def set_model(self, model: str) -> None:
        self.model = model

    def set_year(self, year: int) -> None:
        self.year = year

    def calculate_age(self) -> int:
        return int(str(date.today()).split("-")[0]) - self.year

    def __str__(self) -> str:
        return f"Car({self.brand}, {self.model}, {self.year})"

    def __repr__(self) -> str:
        return str(self)

    def __lt__(self, other: Car) -> bool:
        return self.year < other.get_year()


class Garage:
    def __init__(self) -> None:
        self.cars: List[Car] = []

    def add_car(self, car: Car) -> None:
        self.cars.append(car)

    def remove_car(self, car: Car) -> None:
        self.cars.remove(car)

    def oldest_car(self) -> Car:
        return min(self.cars)

    def __str__(self) -> str:
        return f"Garage{tuple(self.cars)}"
