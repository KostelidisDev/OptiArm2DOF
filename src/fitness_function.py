from utils import calculate_min_reach, calculate_max_reach


def fitness_function(
        chromosome: tuple[float, ...],
        min_distance: float,
        max_distance: float
) -> float:
    gene_a, gene_b = chromosome
    min_reach = calculate_min_reach(gene_a, gene_b)
    max_reach = calculate_max_reach(gene_a, gene_b)

    diff_of_min = abs(min_reach - min_distance)
    diff_of_max = abs(max_reach - max_distance)

    return -(diff_of_max + diff_of_min)
