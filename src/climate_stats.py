import numpy as np
from itertools import product
from scipy.stats import percentileofscore
from typing import List


def calc_percentile_3d_array(
        data: np.array,
        index_of_score: int,
        axis: int = 0
) -> np.array:
    '''
    Calculates the percentile for a value at a user-defined index based on 
    other values over one axis in a 3d array.
    
    :param data: The 3d data (e.g., time x lat x lon)
    :type data: np.array
    :param index_of_score: Index of value to calc score for
    :type index_of_score: int
    :param axis: Over which axis (default = 0; e.g., time)
    :type axis: int
    :return: a 2d array containing percentiles
    :rtype: np.array
    '''

    if axis > 2:
        raise ValueError("axis must be 0, 1, or 2")

    axis_dict = {}
    try:
        axis_dict[0], axis_dict[1], axis_dict[2] = data.shape
    except:
        raise ValueError(f"data array is not the correct shape: {data.shape}")
    
    # do not want to loop through axis that we are calculating over
    del axis_dict[axis]
    # dimentions to loop through
    len4loop = [v for v in axis_dict.values()]

    a_result = np.empty([len4loop[0], len4loop[1]])
    for j, i in product(range(len4loop[0]), range(len4loop[1])):

        try:
            if axis == 0:
                a = data[:,j,i]
                s = data[index_of_score,j,i]
            elif axis == 1:
                a = data[j,:,i]
                s = data[j, index_of_score, i]
            else:
                a = data[j,i,:]
                s = data[j, i, index_of_score]
        
            a_result[j,i] = percentileofscore(a, s)

        except:
            raise ValueError(
                f"""{j} or {i} is too big for calc over axis {axis} 
                for shape {data.shape}
                """)
        
    return a_result