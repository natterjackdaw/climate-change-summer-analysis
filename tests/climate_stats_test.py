import numpy as np
from scipy.stats import percentileofscore
import random

import pytest

from src.climate_stats import calc_percentile_over_time



def test_calc_percentile_over_time():

    not_3d_array = np.random.rand(2,3,4,2,2)
    expected_error = f"data array is not the correct shape: \{not_3d_array.shape\}"
    
    with pytest.raises(ValueError, match=expected_error):
        calc_percentile_over_time(not_3d_array, 0)


    test_array = np.random.rand(12, 9, 8)

    # test the shape is expected
    random_index = random.randrange(0, 12)
    result_from_3d = calc_percentile_over_time(test_array, random_index)
    assert result_from_3d.shape == (9,8)

    # test for axis = 0
    array1d = test_array[:,2,3]
    result1d = percentileofscore(array1d, array1d[5])
    result_from_3d = calc_percentile_over_time(test_array, 5)
    assert result1d == result_from_3d[2,3], "Compare part to 1d result"