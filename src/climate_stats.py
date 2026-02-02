import numpy as np
from itertools import product
from scipy.stats import percentileofscore
from typing import List


def calc_percentile_over_time(
        data: np.array,
        index_of_score: int
) -> np.array:
    '''
    Calculates the percentile for a value at a user-defined index based on 
    other values over axis = 0 in a 3d array.
    
    :param data: The 3d data (e.g., time x lat x lon)
    :type data: np.array
    :param index_of_score: Index of value to calc score for
    :type index_of_score: int
    :return: a 2d array containing percentiles
    :rtype: np.array
    '''

    axis_dict = {}
    try:
        axis_dict[0], axis_dict[1], axis_dict[2] = data.shape
    except:
        raise ValueError(f"data array is not the correct shape: {data.shape}")
    
    a_result = np.empty([axis_dict[1], axis_dict[2]])
    for j, i in product(range(axis_dict[1]), range(axis_dict[2])):

        a = data[:,j,i]
        s = data[index_of_score,j,i]
    
        a_result[j,i] = percentileofscore(a, s)
        
    return a_result