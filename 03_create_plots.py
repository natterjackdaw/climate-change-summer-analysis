import os
import numpy as np
import xarray as xr

import matplotlib.pyplot as plt

from src.climate_stats import (
    calc_percentile_over_time,
    highest_so_far
)
from src.map_helpers import one_summery_summary_plot


data_dir = f"{os.getcwd()}/data"
data_path = f"{data_dir}/summer_mean_2m_temperature_europe_1950-2025.nc"
ds = xr.open_dataset(data_path, engine="netcdf4")

# plot for 2019 - 2025
years_to_analyse = [y for y in range(2019, 2026)]
# years_to_analyse = [2019] # for testing

# convert to numpy
da = ds["t2m"].to_numpy()
lons = ds["longitude"].to_numpy()
lats = ds["latitude"].to_numpy()
years = ds["year"].to_numpy().tolist()

for year2plot in years_to_analyse:

    print(year2plot)

    year_index = years.index(year2plot)
    da_one_year = da[year_index,:,:]

    print(year_index, da.shape, da_one_year.shape)

    # percentile of temperature compared to 1970-2025
    percentile_to_plot = calc_percentile_over_time(da, year_index)
    print(percentile_to_plot)

    # is this the hotest temperature so far over 1950-2025?
    hottest_to_shade = highest_so_far(da, year_index)
    print(hottest_to_shade)

    print(percentile_to_plot.dtype)
    print(hottest_to_shade.dtype)

    print('plotting...')

    fig = one_summery_summary_plot(
        percentile_to_plot,
        hottest_to_shade,
        lats, lons
    )

    image_path = f'images/average_summer_temp_comparison_{year2plot}.png'
    print(f'saving as... {image_path}')
    plt.savefig(image_path)