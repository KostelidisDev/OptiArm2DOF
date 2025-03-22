from geneal.genetic_algorithms import ContinuousGenAlgSolver

from config import Config, get_config
from fitness_function import fitness_function
from utils import calculate_min_reach, calculate_max_reach


def main(config: Config) -> None:
    print("*" * 10)
    print("OptiArm2DOF")
    print("Developed by Iordanis Kostelidis <iordkost@ihu.gr>")
    print("This project was conducted as part of the course Ρ202: Mechanical Intelligence "
          "in the M.Sc. program in Robotics, offered by the Department of "
          "Computer, Informatics and Telecommunications Engineering at the "
          "International Hellenic University.")
    print("*" * 10)

    print("Initializing genetic algorithm...")
    print("\tConfiguration:")
    config.log()

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

    print("Running genetic algorithm...")
    solver.solve()
    best_chromosome = solver.best_individual_
    gene_a, gene_b = best_chromosome
    min_distance = calculate_min_reach(gene_a, gene_b)
    max_distance = calculate_max_reach(gene_a, gene_b)

    print("Results")
    print(f"\tgene_a: {gene_a:.4f}, gene_b: {gene_b:.4f}")
    print(f"\tMin Distance: {min_distance}, Max Distance: {max_distance}")


if __name__ == '__main__':
    main(get_config())
