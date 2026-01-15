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

# year to plot analysis for (don't look at years after)
year2plot = 2025

ds = xr.open_dataset(data_path, engine="netcdf4")
ds_stop_at_year2plot = ds.where(ds["year"]<=year2plot)

# convert to numpy
da = ds_stop_at_year2plot["t2m"].to_numpy()
lons = ds["longitude"].to_numpy()
lats = ds["latitude"].to_numpy()
years = ds["year"].to_numpy().tolist()
print(da.shape, lons.shape, lats.shape)
year_index = years.index(2025)

# calculate the maximum mean summer temperature
max_summer = da.max(axis=0)
print(max_summer.shape)
# extract the latest mean summer temperature
latest_year = da[year_index,:,:]

diff = latest_year - max_summer

is_hottest = np.where(diff == 0, 1, None)
print(is_hottest.shape)

# convert lats and lons to list
# lats = lats.tolist()
# lons = lons.tolist()

# print(lons)
# print(lats)

# plot
# create the figure and axes instances.

fig = plt.figure()
ax = fig.add_subplot(1,1,1,
                     projection=ccrs.PlateCarree()
                     )
ax.set_extent(
    [lons[0], lons[-1], lats[0], lats[-1]],
    crs=ccrs.PlateCarree()
)

# map = Basemap(
#     lon_0 = 0,
#     llcrnrlat=lats[-1],
#     urcrnrlat=lats[0],
#     llcrnrlon=lons[0],
#     urcrnrlon=lons[-1]
# )

# # test that other data can be plotted under
# conf = ax.contourf(
#     lons, lats, latest_year,
#     zorder=0
#     )

# map.drawcoastlines(linewidth=0.2)
ax.add_feature(cfeature.COASTLINE, lw=0.2)
ax.add_feature(cfeature.BORDERS, linewidth=0.2)

is_hottest = np.array(is_hottest, dtype=float)
# not sure what this does yet
# is_hottest, lons = addcyclic(is_hottest, lons)
# xx, yy   = np.meshgrid(lons,lats)
# xx, yy    = map(xx, yy)

conf = ax.contourf(
    lons, lats, is_hottest,
    colors='white', hatches=['xxxxx'],
    zorder=2
    )


# mask ocean - but only above other data,
# should not mask this data, yet it does...
ax.add_feature(cartopy.feature.OCEAN, 
               color = '#DEFFFF',
               zorder=1)
# fig.colorbar(conf,orientation='horizontal')

plt.savefig('images/test.png')
