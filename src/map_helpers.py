import numpy as np
from typing import List

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

import cartopy
import cartopy.crs as ccrs
import cartopy.feature as cfeature


def one_summery_summary_plot(
    percentile_data: np.array,
    hottest_so_far_data: np.array,
    lats: np.array | List,
    lons: np.array | List,
    hatch_style: str = "xxx"
) -> mpl.figure.Figure:
    """
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
    :param lats: Latitude (y-axis) of data
    :type lats: np.array | List
    :param lons: Longitude (x-axis) of data
    :type lons: np.array | List
    :return: The plot object we want out (hopefully)
    :rtype: matplotlib figure
    :param hatch_style: what hatching to put in areas where it is hottest so far
    :rtype: str
    """

    if percentile_data.shape != hottest_so_far_data.shape:
        raise ValueError("shape of percentile_data and hottest_so_far do not match")

    if percentile_data.ndim != 2:
        raise ValueError("Make sure that arrays are 2d")

    if percentile_data.size != len(lats) * len(lons):
        raise ValueError("lats and lons do not match shape of array")

    # make sure that hottest is dtype int
    if hottest_so_far_data.dtype == object:
        hottest_so_far_data = hottest_so_far_data.astype(np.float64)

    # only one plot per figure
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    ax.set_extent([lons[0], lons[-1], lats[0], lats[-1]], crs=ccrs.PlateCarree())

    ax.add_feature(cfeature.COASTLINE, lw=0.2)
    ax.add_feature(cfeature.BORDERS, linewidth=0.2)

    conf = ax.contourf(
        lons,
        lats,
        percentile_data,
        levels=[20, 30, 40, 50, 60, 70, 80],
        cmap="coolwarm",
        zorder=1,
        extend="both",
    )

    ax.contourf(
        lons, lats, hottest_so_far_data, colors="none", 
        hatches=[hatch_style], zorder=2
    )

    ax.add_feature(cartopy.feature.OCEAN, color="#DEFFFF", zorder=3)

    fig.colorbar(conf, orientation="vertical", ax=ax)

    legend_elements = [
        Patch(hatch=hatch_style)
    ]
    ax.legend(handles=legend_elements, loc='right')

    return fig
