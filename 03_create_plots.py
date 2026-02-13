import os
import numpy as np
import xarray as xr

import matplotlib.pyplot as plt

from src.climate_stats import calc_percentile_over_time
from src.map_helpers import one_summery_summary_plot


data_dir = f"{os.getcwd()}/data"
data_path = f"{data_dir}/summer_mean_2m_temperature_europe_1950-2025.nc"

# plot for 2019 - 2025
years = [y for y in range(2019,2026)]

# convert to numpy
da = ds["t2m"].to_numpy()
lons = ds["longitude"].to_numpy()
lats = ds["latitude"].to_numpy()
years = ds["year"].to_numpy().tolist()

for year2plot in years:

    year_index = years.index(year2plot)
    da_one_year = da[year_index,:,:]

    

