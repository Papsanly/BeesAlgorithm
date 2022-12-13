from abc import abstractmethod, ABC
from dataclasses import dataclass
from typing import Type, Any, Callable, Self


class OptimizedAlgorithm(ABC):

    def __init__(self, problem: Any, **kwargs):
        self.problem = problem
        self.execution_time = None

    @abstractmethod
    def solve(self) -> Any:
        pass

    def get_execution_time(self) -> float:
        if self.execution_time is not None:
            return self.execution_time


@dataclass
class AlgorithmResult:
    objective_value: Callable
    parameters: dict[str, float]

    def __lt__(self, other: Self) -> bool:
        return self.objective_value < other.objective_value

    def __gt__(self, other: Self) -> bool:
        return self.objective_value > other.objective_value


def evaluate_in_range(
        algorithm_class: Type[OptimizedAlgorithm],
        problem: Any,
        objective_function: Callable,
        max_execution_time: float,
        fixed_params: dict[str, float],
        param_name: str,
        start: int,
        end: int,
        step: int,
        repeats: int
) -> list[AlgorithmResult]:

    results = []

    for value in range(start, end, step):
        params = {**fixed_params, param_name: value}
        algorithm = algorithm_class(problem, **params)
        result = sum(objective_function(algorithm.solve()) for _ in range(repeats)) / repeats
        if algorithm.get_execution_time() > max_execution_time:
            if not results:
                return [AlgorithmResult(result, params)]
            return results
        results.append(AlgorithmResult(result, params))

    return results


def optimize_algorithm(
        algorithm: Type[OptimizedAlgorithm],
        problem: Any,
        parameters: dict[str, tuple[int, int, int]],
        objective_function: Callable,
        max_execution_time: float,
        iterations: int = 10,
        repeats: int = 10
) -> dict[str, float]:
    params_list = list(parameters.keys())
    param_idx = 0
    fixed_params = {k: v[0] for k, v in parameters.items()}
    for i in range(iterations):
        param_name = params_list[param_idx]

        fixed_params.pop(param_name)

        best_result = max(evaluate_in_range(
            algorithm, problem, objective_function, max_execution_time,
            fixed_params, param_name, *parameters[param_name], repeats
        ))
        print(f'Iteration {i}: {best_result.objective_value}')
        fixed_params[param_name] = best_result.parameters[param_name]

        param_idx = (param_idx + 1) % len(params_list)

    return fixed_params
