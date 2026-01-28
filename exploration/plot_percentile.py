import os
import numpy as np
import xarray as xr

from mpl_toolkits.basemap import Basemap, addcyclic
import matplotlib.pyplot as plt

import cartopy
import cartopy.crs as ccrs
import cartopy.feature as cfeature


data_dir = f"{os.getcwd()}/data"
data_path = f"{data_dir}/summer_mean_2m_temperature_europe_1950-2025.nc"

# year to calculate percentile for (compared to whole period 1950-2025)
year2plot = 2025

ds = xr.open_dataset(data_path, engine="netcdf4")

# convert to numpy
da = ds["t2m"].to_numpy()
lons = ds["longitude"].to_numpy()
lats = ds["latitude"].to_numpy()
years = ds["year"].to_numpy().tolist()
print(da.shape, lons.shape, lats.shape)

# calc percentile


year_index = years.index(year2plot)


