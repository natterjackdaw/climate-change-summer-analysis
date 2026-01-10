import numpy as np
from typing import List


def convert_measurements_to_percentile_one_direction(
        measurements: List
):
    
    sorted_measurements = measurements.sorted()

    percentile_spacing = 100./len(measurements)
    available_percentiles = range(percentile_spacing, 100. + percentile_spacing)
    
    print(len(measurements), len(available_percentiles))
    print(available_percentiles)


if __name__ == "main":

    rough_test = [25, 100, 50, 32]

    out_test = convert_measurements_to_percentile_one_direction(rough_test)