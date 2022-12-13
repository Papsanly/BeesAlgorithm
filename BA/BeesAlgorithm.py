import time

from BA.Bee import Bee
from BA.BeesProblem import BeesProblem
from optimize import OptimizedAlgorithm


class BeesAlgorithm(OptimizedAlgorithm):

    def __init__(
            self,
            problem: BeesProblem,
            foragers: int,
            scouts: int,
            max_iterations: int = 1000
    ):
        super().__init__(problem)
        self.problem = problem
        self.foragers_count = foragers
        self.scouts_count = scouts
        self.bees = self._scout(foragers + scouts)
        self.max_iterations = max_iterations
        self.execution_time = None

    def solve(self) -> Bee:
        start = time.time()
        for _ in range(self.max_iterations):
            forager_bees = self._forage(self.foragers_count)
            scout_bees = self._scout(self.scouts_count)
            self.bees = forager_bees + scout_bees

        self.execution_time = time.time() - start
        return max(self.bees)

    def _forage(self, count) -> list[Bee]:
        return [
            self.problem.get_neighbor(forage_bee)
            for forage_bee in sorted(self.bees, reverse=True)[:count]
        ]

    def _scout(self, count: int) -> list[Bee]:
        return [self.problem.get_bee() for _ in range(count)]
