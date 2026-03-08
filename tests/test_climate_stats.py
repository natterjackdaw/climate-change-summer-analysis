from itertools import product
import numpy as np
from scipy.stats import percentileofscore
import random
import re

import pytest

from src.climate_stats import calc_percentile_over_time, highest_so_far


def test_calc_percentile_over_time():

    not_3d_array = np.random.rand(2, 3, 4, 2, 2)
    expected_error = re.escape(
        f"data array is not the correct shape: {not_3d_array.shape}"
    )

    with pytest.raises(ValueError, match=expected_error):
        calc_percentile_over_time(not_3d_array, 0)

    test_array = np.random.rand(12, 9, 8)

    # test the shape is expected
    random_index = random.randrange(0, 12)
    result_from_3d = calc_percentile_over_time(test_array, random_index)
    assert result_from_3d.shape == (9, 8)

    # test for axis = 0
    array1d = test_array[:, 2, 3]
    result1d = percentileofscore(array1d, array1d[5])
    result_from_3d = calc_percentile_over_time(test_array, 5)
    assert result1d == result_from_3d[2, 3]


def test_highest_so_far_errors():

    too_small = np.array([[1, 2], [3, 4]])

    ok_array = np.array(
        [[[1, 2, 3], [1, 2, 3], [5, 6, 7]], [[2, 3, 4], [3, 4, 5], [5, 4, 6]]]
    )

    expected_error = re.escape(
        "You need data (2, 2) to be 3D and year_index (1) to be equal to or more than first axis"
    )
    with pytest.raises(ValueError, match=expected_error):
        highest_so_far(too_small, 1)

    expected_error = re.escape(
        "You need data (2, 3, 3) to be 3D and year_index (54) to be equal to or more than first axis"
    )
    with pytest.raises(ValueError, match=expected_error):
        highest_so_far(ok_array, 54)


def test_highest_so_far_result():

    input = np.array(
        [
            [[23, 8, 6, 2], [5, 6, 32, 76], [99, 3, 3, 1]],
            [[4, 5, 83, 0], [100, 200, 5, 2], [54, 6, 2, 3]],
        ]
    )
    print(input.shape)

    # by definition if y index = 0  then all 1
    expected0 = np.array([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]])
    actual0 = highest_so_far(input, 0)

    expected1 = np.array(
        [[None, None, 1, None], [1, 1, None, None], [None, 1, None, 1]]
    )
    actual1 = highest_so_far(input, 1)

    assert actual0.shape == expected0.shape
    assert actual1.shape == expected1.shape

    print(expected1)
    print(actual1)

    for j, i in product(range(2), range(2)):
        assert actual0[j, i] == expected0[j, i]
        assert actual1[j, i] == expected1[j, i]
