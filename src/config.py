import os
from typing import Tuple


class Config:
    lower_bound: int = 1
    upper_bound: int = 150
    min_distance: int = 70
    max_distance: int = 150
    n_genes: int = 2
    max_gen: int = 50
    pop_size: int = 10
    mutation_rate: float = 0.15
    selection_rate: float = 0.5
    selection_strategy: str = "roulette_wheel"
    verbose: bool = False
    show_stats: bool = False
    plot_stats: bool = True
    variables_type: type = int
    fitness_tolerance: bool = False
    fitness_tolerance_diff: float = 1
    fitness_tolerance_gen: int = 50

    def get_variables_limits(self) -> Tuple[int, int]:
        return self.lower_bound, self.upper_bound

    def get_fitness_tolerance(self) -> Tuple[float, float] or None:
        if self.fitness_tolerance is False:
            return None
        return self.fitness_tolerance_diff, self.fitness_tolerance_gen

    def set_lower_bound(self, lower_bound: int):
        self.lower_bound = int(lower_bound)

    def set_upper_bound(self, upper_bound: int):
        self.upper_bound = int(upper_bound)

    def set_min_distance(self, min_distance: int):
        self.min_distance = int(min_distance)

    def set_max_distance(self, max_distance: int):
        self.max_distance = int(max_distance)

    def set_n_genes(self, n_genes: int):
        self.n_genes = int(n_genes)

    def set_max_gen(self, max_gen: int):
        self.max_gen = int(max_gen)

    def set_pop_size(self, pop_size: int):
        self.pop_size = int(pop_size)

    def set_mutation_rate(self, mutation_rate: float):
        self.mutation_rate = float(mutation_rate)

    def set_selection_rate(self, selection_rate: float):
        self.selection_rate = float(selection_rate)

    def set_selection_strategy(self, selection_strategy: str):
        self.selection_strategy = selection_strategy

    def set_verbose(self, verbose: str):
        self.verbose = verbose == "True"

    def set_show_stats(self, show_stats: bool):
        self.show_stats = show_stats == "True"

    def set_plot_stats(self, plot_stats: str):
        self.plot_stats = plot_stats == "True"

    def set_variables_type(self, variables_type: str):
        if variables_type == "int":
            self.variables_type = int
            return
        if variables_type == "float":
            self.variables_type = float
            return
        self.variables_type = int

    def set_fitness_tolerance(self, fitness_tolerance: str):
        self.fitness_tolerance = fitness_tolerance == "True"

    def set_fitness_tolerance_diff(self, fitness_tolerance_diff: float):
        self.fitness_tolerance_diff = float(fitness_tolerance_diff)

    def set_fitness_tolerance_gen(self, fitness_tolerance_gen: int):
        self.fitness_tolerance_gen = int(fitness_tolerance_gen)

    def log(self):
        print(f"\t\tLower Bound: {self.lower_bound}")
        print(f"\t\tUpper Bound: {self.upper_bound}")
        print(f"\t\tMin Distance: {self.min_distance}")
        print(f"\t\tMax Distance: {self.max_distance}")
        print(f"\t\tN Genes: {self.n_genes}")
        print(f"\t\tMax Gen: {self.max_gen}")
        print(f"\t\tPop Size: {self.pop_size}")
        print(f"\t\tMutation Rate: {self.mutation_rate}")
        print(f"\t\tSelection Rate: {self.selection_rate}")
        print(f"\t\tSelection Strategy: {self.selection_strategy}")
        print(f"\t\tVerbose: {self.verbose}")
        print(f"\t\tShow Stats: {self.show_stats}")
        print(f"\t\tPlot Stats: {self.plot_stats}")
        print(f"\t\tVariables Type: {self.variables_type}")
        print(f"\t\tFitness Tolerance: {self.fitness_tolerance}")
        print(f"\t\tFitness Tolerance Diff: {self.fitness_tolerance_diff}")
        print(f"\t\tFitness Tolerance Gen: {self.fitness_tolerance_gen}")


def get_config() -> Config:
    if not os.path.exists(".env"):
        return Config()

    parsed = {}
    with open(".env") as f:
        for line in f.readlines():
            line = line.strip()
            if line == "":
                continue
            if line.startswith("#"):
                continue
            key, value = line.split("=", 1)
            parsed[key] = value
        f.close()

    config = Config()
    key_to_config_set_function = {
        "LOWER_BOUND": config.set_lower_bound,
        "UPPER_BOUND": config.set_upper_bound,
        "MIN_DISTANCE": config.set_min_distance,
        "MAX_DISTANCE": config.set_max_distance,
        "MAX_GEN": config.set_max_gen,
        "POP_SIZE": config.set_pop_size,
        "MUTATION_RATE": config.set_mutation_rate,
        "SELECTION_RATE": config.set_selection_rate,
        "SELECTION_STRATEGY": config.set_selection_strategy,
        "VERBOSE": config.set_verbose,
        "SHOW_STATS": config.set_show_stats,
        'PLOT_STATS': config.set_plot_stats,
        "VARIABLES_TYPE": config.set_variables_type,
        "FITNESS_TOLERANCE": config.set_fitness_tolerance,
        "FITNESS_TOLERANCE_DIF": config.set_fitness_tolerance_diff,
        "FITNESS_TOLERANCE_GEN": config.set_fitness_tolerance_gen,
    }
    for key, value in parsed.items():
        if key not in key_to_config_set_function:
            continue
        key_to_config_set_function[key](value)
    return config
