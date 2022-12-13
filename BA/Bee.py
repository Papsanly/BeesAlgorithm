from abc import ABC, abstractmethod
from typing import Self


class Bee(ABC):

    def __lt__(self, other: Self) -> bool:
        return self.fitness < other.fitness

    def __gt__(self, other: Self) -> bool:
        return self.fitness > other.fitness

    @property
    @abstractmethod
    def fitness(self) -> float:
        pass
