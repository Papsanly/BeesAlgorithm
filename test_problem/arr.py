from BA.Bee import Bee


class Arr(Bee, list):

    @property
    def fitness(self) -> float:
        return sum(self)
