import numpy as np
import random

import pytest

from src.map_helpers import one_summery_summary_plot


def test_map_helper_errors():

    a1 = np.random.rand(3,4)
    a1_wrong = np.random.rand(5,5)
    a2 = np.random.rand(3,4)
    a2_wrong = np.random.rand(8,2)
    big_random = np.random.rand(8,3,5,2)
    lats = np.random.rand(3)
    lats_wrong = np.random.rand(12)
    lons = np.random.rand(4)
    lons_wrong = np.random.rand(2)

    # do not match
    expected_error = 'shape of percentile_data and hottest_so_far do not match'
    with pytest.raises(ValueError, match=expected_error):
        one_summery_summary_plot(a1, a2_wrong, lats, lons)

    with pytest.raises(ValueError, match=expected_error):
        one_summery_summary_plot(a1_wrong, a2, lats, lons)

    expected_error = "Make sure that arrays are 2d"
    with pytest.raises(ValueError, match=expected_error):
        one_summery_summary_plot(big_random, big_random, lats, lons)

    expected_error = 'lats and lons do not match shape of array'
    with pytest.raises(ValueError, match=expected_error):
        one_summery_summary_plot(a1, a2, lats_wrong, lons)

    with pytest.raises(ValueError, match=expected_error):
        one_summery_summary_plot(a1, a2, lats, lons_wrong)

    with pytest.raises(ValueError, match=expected_error):
        one_summery_summary_plot(a1, a2, list(lats_wrong), list(lons_wrong))