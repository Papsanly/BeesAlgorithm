from BA.BeesAlgorithm import BeesAlgorithm
from clique.CliqueProblem import CliqueProblem
from optimize import optimize_algorithm


def main():
    problem = CliqueProblem(300, (2, 30))

    print('Optimizing...')
    optimized_values = optimize_algorithm(
        BeesAlgorithm,
        problem,
        {'foragers': (1, 100, 5), 'scouts': (1, 40, 2)},
        lambda x: x.fitness,
        0.1,
        iterations=10,
        repeats=10
    )
    print('Done')
    print(f'Best configuration: {optimized_values}')

    algorithm = BeesAlgorithm(problem, **optimized_values)
    print('Solving...')
    solution = algorithm.solve()
    print(f'Best solution: {solution.fitness}')
    print(f'Execution time: {algorithm.execution_time}')


if __name__ == '__main__':
    main()
