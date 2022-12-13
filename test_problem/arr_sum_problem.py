from dataclasses import dataclass
from random import randint

from BA.BeesProblem import BeesProblem
from optimize import OptimizedProblem
from test_problem.arr import Arr


@dataclass
class ArrSumProblem(BeesProblem, OptimizedProblem):

    length: int

    def get_bee(self) -> Arr:
        return Arr([0 for _ in range(self.length)])

    def get_neighbor(self, bee: Arr) -> Arr:
        rand_index = randint(0, len(bee) - 1)
        new_bee = Arr(bee.copy())
        new_bee[rand_index] = 1 - new_bee[rand_index]
        if new_bee > bee:
            return new_bee
        return bee
