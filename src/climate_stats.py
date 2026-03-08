import numpy as np
from itertools import product
from scipy.stats import percentileofscore


def calc_percentile_over_time(data: np.array, index_of_score: int) -> np.array:
    """
    Calculates the percentile for a value at a user-defined index based on
    other values over axis = 0 in a 3d array.

    :param data: The 3d data (e.g., time x lat x lon)
    :type data: np.array
    :param index_of_score: Index of value to calc score for
    :type index_of_score: int
    :return: a 2d array containing percentiles
    :rtype: np.array
    """

    axis_dict = {}
    try:
        axis_dict[0], axis_dict[1], axis_dict[2] = data.shape
    except ValueError:
        raise ValueError(f"data array is not the correct shape: {data.shape}")
    except Exception as E:
        print(E)

    a_result = np.empty([axis_dict[1], axis_dict[2]])
    for j, i in product(range(axis_dict[1]), range(axis_dict[2])):
        a = data[:, j, i]
        s = data[index_of_score, j, i]

        a_result[j, i] = percentileofscore(a, s)

    return a_result


def highest_so_far(data: np.array, year_index: int) -> np.array:
    """
    Returns an array filled with 1 and None.
    1 where that area for that year was the highest value so far
    None where this is not true.
    So if index is 0, it will return an array with all 1s

    :param data: A 3D array (years, lats, lons)
    :type data: np.array
    :param year_index: The index for the year that you want to know about
    :type year_index: int
    :return: Description
    :rtype: np.array
    """
    try:
        years_so_far = data[:year_index, :, :]
        latest_year = data[year_index, :, :]
    except ValueError:
        raise ValueError(
            f"""You need data {data.shape} to be 3D and year_index ({year_index}) to be equal to or more than first axis"""
        )
    except Exception as E:
        print(E)

    if year_index == 0:
        # by definition, first year will have highest values so far
        return np.full(latest_year.shape, 1)
    else:
        # if value is more than max value of previous years
        # then it must be highest so far
        max_summer = years_so_far.max(axis=0)
        return np.where(latest_year >= max_summer, 1, None)


if __name__ == "__main__":
    random_input = np.random.rand(2, 2, 2)
    print(random_input)

    print()
    output = highest_so_far(random_input, 0)
    print(output.shape)
    print(output)

    print()
    output = highest_so_far(random_input, 1)
    print(output.shape)
    print(output)
