from BA.BeesAlgorithm import BeesAlgorithm
from clique.CLiqueProblem import CliqueProblem
from optimize import optimize_algorithm


def main():
    optimized_values = optimize_algorithm(
        BeesAlgorithm(),
        CliqueProblem()
    )


if __name__ == '__main__':
    main()
