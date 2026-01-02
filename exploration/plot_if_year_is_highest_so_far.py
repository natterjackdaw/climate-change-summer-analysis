import os
import numpy as np
import xarray as xr

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt


data_dir = f"{os.getcwd()}/data"
data_path = f"{data_dir}/summer_mean_2m_temperature_europe_1950-2025.nc"

# year to plot analysis for (don't look at years after)
year2plot = 2025

ds = xr.open_dataset(data_path, engine="netcdf4")
ds_stop_at_year2plot = ds.where(ds["year"]<=year2plot)

# convert to numpy
da = ds_stop_at_year2plot["t2m"].to_numpy()
lons = ds["longitude"].to_numpy()
lats = ds["latitude"].to_numpy()
print(da.shape, lons.shape, lats.shape)

# calculate the maximum mean summer temperature
max_summer = da.max(axis=0)
print(max_summer.shape)
# extract the latest mean summer temperature
latest_year = da[-1,:,:]

diff = latest_year - max_summer

is_hottest = np.where(diff == 0, 1, None)
print(is_hottest.shape)

# convert lats and lons to list
lats = lats.tolist()
lons = lons.tolist()

# plot
# create the figure and axes instances.

fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])


