from geneal.genetic_algorithms import ContinuousGenAlgSolver

from config import get_config
from fitness_function import fitness_function


def main():
    config = get_config()
    generations_test_cases = [50, 100, 150, 200]
    populations_test_cases = [10, 30, 50, 70]
    iterations_per_test_case_pair = list(range(1, 11))

    results = {}

    for generations in generations_test_cases:
        for populations in populations_test_cases:

            config.set_max_gen(generations)
            config.set_pop_size(populations)

            for iteration in iterations_per_test_case_pair:
                solver = ContinuousGenAlgSolver(
                    n_genes=config.n_genes,
                    fitness_function=lambda chromosome: fitness_function(
                        chromosome,
                        config.min_distance,
                        config.max_distance
                    ),
                    max_gen=config.max_gen,
                    pop_size=config.pop_size,
                    mutation_rate=config.mutation_rate,
                    selection_rate=config.selection_rate,
                    selection_strategy=config.selection_strategy,
                    verbose=config.verbose,
                    show_stats=config.show_stats,
                    plot_results=config.plot_stats,
                    variables_limits=config.get_variables_limits(),
                    variables_type=config.variables_type,
                    fitness_tolerance=config.get_fitness_tolerance()
                )
                solver.solve()
                best_fitness = solver.best_fitness_
                generations_populations_pair = f"{generations}/{populations}"
                if generations_populations_pair not in results:
                    results[generations_populations_pair] = {}
                if iteration not in results[generations_populations_pair]:
                    results[generations_populations_pair][iteration] = best_fitness


    test_result_text = ""

    first_line = True
    for generations_populations_pair, generations_populations_iterations_results in results.items():
        if first_line:
            first_line_text = ""
            for iteration_number in iterations_per_test_case_pair:
                first_line_text += f",{iteration_number}"
            test_result_text += f"{first_line_text}"
            first_line = False
        line_text = f"{generations_populations_pair}"
        for iteration_number, iteration_result in generations_populations_iterations_results.items():
            line_text += f",{iteration_result}"
        test_result_text += f'\n{line_text}'

    print(test_result_text)
    with open("test_result.csv", "w") as f:
        f.write(test_result_text)
        f.close()


if __name__ == '__main__':
    main()
