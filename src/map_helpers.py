import numpy as np
from typing import List, Dict

import matplotlib.pyplot as plt
import matplotlib.figure

import cartopy
import cartopy.crs as ccrs
import cartopy.feature as cfeature

def one_summery_summary_plot(
    percentile_data: np.array,
    hottest_so_far_data: np.array,
    lats: np.array | List,
    lons: np.array | List
):
    '''
    Returns plot of:
    * an array of values that are 1 or None
    * an array of percentile values

    percentile_data and hottest_so_far_data need to be the same shape.
    They need to be of shape (lats, lons).
    
    :param percentile_data: Percentile values (-100 - 100)
    :type percentile_data: np.array
    :param hottest_so_far_data: All data points are 1 or null for plotting
    :type hottest_so_far_data: np.array
    :param lats: Latitude
    :type lats: np.array | List
    :param lons: Description
    :type lons: np.array | List
    '''
    

    if percentile_data.shape != hottest_so_far_data.shape:
        raise ValueError(
            'shape of percentile_data and hottest_so_far do not match'
            )
    
    if percentile_data.ndim != 2:
        raise ValueError('Make sure that arrays are 2d')
    
    if percentile_data.size != len(lats) * len(lons):
        raise ValueError('lats and lons do not match shape of array')
    
