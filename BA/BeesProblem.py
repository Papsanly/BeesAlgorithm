from abc import ABC, abstractmethod
from BA.Bee import Bee


class BeesProblem(ABC):

    @abstractmethod
    def get_bee(self) -> Bee:
        pass

    @abstractmethod
    def get_neighbor(self, bee: Bee) -> Bee:
        pass
