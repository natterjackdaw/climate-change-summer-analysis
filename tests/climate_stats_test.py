import numpy as np
from scipy.stats import percentileofscore

import pytest
from climate_stats import calc_percentile_3d_array


def test_calc_percentile_3d_array():

    not_3d_array = np.random.rand(2,3,4,2,2)
    expected_error = f"data array is not the correct shape: {not_3d_array.shape}"
    
    with pytest.raises(ValueError, match=expected_error):
        calc_percentile_3d_array(not_3d_array, 0, 2)


    test_array = np.random.rand(12, 9, 8)

    # test for axis = 0
    array1d = test_array[:,2,3]
    result1d = percentileofscore(array1d, array1d[5])
    result_from_3d = calc_percentile_3d_array(test_array, 5)
    assert result1d == result_from_3d[2,3], "zeroth axis test"

    # test for axis = 1
    array1d = test_array[5,:,3]
    result1d = percentileofscore(array1d, array1d[1])
    result_from_3d = calc_percentile_3d_array(test_array, 1)
    assert result1d == result_from_3d[5,3], "first axis test"


    with pytest.raises(ValueError, match="axis must be 0, 1, or 2"):
        calc_percentile_3d_array(not_3d_array, 0, 10)

    
