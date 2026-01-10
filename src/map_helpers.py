import numpy as np
from typing import List, Dict

def rearrange_for_prime_meridian(
    map_data: np.numpy,
    lons: List
) -> Dict:
    '''
    Re-arranges data so that it may be mapped with a focus on Europe or Africa 
    (i.e., the starting point is not 0, and there are negative latitudes, 
    rather than 0-360).
    
    :param map_data: The data to be mapped on a plot.
    :type map_data: np.numpy
    :param lons: The latitudes represented by the data.
    :type lons: List
    :return: The converted latitude and data.
    :rtype: Dict
    '''
    # check that the shape of array matches the length of the longitude points