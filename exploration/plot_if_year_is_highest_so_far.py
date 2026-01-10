import os
import numpy as np
import xarray as xr

from mpl_toolkits.basemap import Basemap, addcyclic
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

is_hottest = np.where(diff == 0, 1, 0)
print(is_hottest.shape)

# convert lats and lons to list
# lats = lats.tolist()
# lons = lons.tolist()

# print(lons)
# print(lats)

# plot
# create the figure and axes instances.

fig = plt.figure()
# ax = fig.add_axes([0.05,0.1,0.9,0.9])

map = Basemap(
    lon_0 = 0,
    llcrnrlat=lats[-1],
    urcrnrlat=lats[0],
    llcrnrlon=lons[0],
    urcrnrlon=lons[-1]
)

map.drawcoastlines(linewidth=0.2)
is_hottest = np.array(is_hottest, dtype=float)
# not sure what this does yet
is_hottest, lons = addcyclic(is_hottest, lons)
xx, yy   = np.meshgrid(lons,lats)
xx, yy    = map(xx, yy)

conf = map.contourf(xx, yy, is_hottest)
fig.colorbar(conf,orientation='horizontal')


plt.savefig('images/test.png')
