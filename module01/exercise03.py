"""Interfaces vs. abstract classes with abc.ABC."""
from abc import ABC, abstractmethod


class Pet(ABC):
    """Interface: abstract members only, no state."""

    @property
    @abstractmethod
    def name(self) -> str: ...

    @name.setter
    @abstractmethod
    def name(self, name: str) -> None: ...

    @abstractmethod
    def play(self) -> None: ...


class Animal(ABC):
    """Abstract class: shared state and behaviour, plus abstract methods left to subclasses."""

    def __init__(self, legs: int) -> None:
        self.__legs = legs

    @property
    def legs(self) -> int:
        return self.__legs

    # concrete method
    def walk(self) -> None:
        print(f"Animal with {self.legs} legs is walking now...")

    @abstractmethod
    def eat(self) -> None: ...


class Spider(Animal):
    def __init__(self) -> None:
        super().__init__(legs=8)

    def eat(self) -> None:
        print("Spider is eating now...")


class Cat(Animal, Pet):
    def __init__(self, name: str = "Tekir") -> None:
        super().__init__(legs=4)
        self.__name = name

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    def eat(self) -> None:
        print(f"{self.name} is eating now...")

    def play(self) -> None:
        print(f"{self.name} is playing now...")


def main() -> None:
    zoo_animals: list[Animal] = [Spider(), Cat("Garfield"), Cat(), Spider()]
    for animal in zoo_animals:
        animal.walk()
        animal.eat()
        if isinstance(animal, Pet):
            animal.play()


if __name__ == "__main__":
    main()
