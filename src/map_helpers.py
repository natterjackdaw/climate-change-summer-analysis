import numpy as np
from typing import List

import matplotlib.pyplot as plt

import cartopy
import cartopy.crs as ccrs
import cartopy.feature as cfeature

def one_summery_summary_plot(
    percentile_data: np.array,
    hottest_so_far_data: np.array,
    lats: np.array | List,
    lons: np.array | List
) -> plt.figure:
    '''
    Docstring for one_summery_summary_plot
    
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
    :return: The plot object we want out (hopefully)
    :rtype: matplotlib figure
    '''
    
    if percentile_data.shape != hottest_so_far_data.shape:
        raise ValueError(
            'shape of percentile_data and hottest_so_far do not match'
            )
    
    if percentile_data.ndim != 2:
        raise ValueError('Make sure that arrays are 2d')
    
    if percentile_data.size != len(lats) * len(lons):
        raise ValueError('lats and lons do not match shape of array')
    
    # only one plot per figure
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1,
                        projection=ccrs.PlateCarree()
                        )
    ax.set_extent(
        [lons[0], lons[-1], lats[0], lats[-1]],
        crs=ccrs.PlateCarree()
    )

    ax.add_feature(cfeature.COASTLINE, lw=0.2)
    ax.add_feature(cfeature.BORDERS, linewidth=0.2)

    conf = ax.contourf(
        lons, lats, percentile_data,
        levels = [20, 30, 40, 50, 60, 70, 80],
        cmap='coolwarm',
        zorder=1,
        extend='both'
        )
    
    conf_bool = ax.contourf(
        lons, lats, hottest_so_far_data,
        #colors='white', 
        hatches=['xxxxx'],
        zorder=2
        )

    ax.add_feature(cartopy.feature.OCEAN, 
               color = '#DEFFFF',
               zorder=3)

    fig.colorbar(conf, orientation='horizontal')

    return fig