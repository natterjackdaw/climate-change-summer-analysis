import os
from itertools import product

import numpy as np
import xarray as xr

from scipy.stats import percentileofscore

from mpl_toolkits.basemap import Basemap, addcyclic
import matplotlib.pyplot as plt

import cartopy
import cartopy.crs as ccrs
import cartopy.feature as cfeature


data_dir = f"{os.getcwd()}/data"
data_path = f"{data_dir}/summer_mean_2m_temperature_europe_1950-2025.nc"

# year to calculate percentile for (compared to whole period 1950-2025)
year2plot = 2020

ds = xr.open_dataset(data_path, engine="netcdf4")

# convert to numpy
da = ds["t2m"].to_numpy()
lons = ds["longitude"].to_numpy()
lats = ds["latitude"].to_numpy()
years = ds["year"].to_numpy().tolist()
print(da.shape, lons.shape, lats.shape)

year_index = years.index(year2plot)
da_one_year = da[year_index,:,:]

# calc percentile
da_result = np.empty(shape=da_one_year.shape)

for j, i in product(range(len(lats)), range(len(lons))):

    a = da[:,j,i]
    s = da_one_year[j,i]
    da_result[j,i] = percentileofscore(a, s)

# PLOT

fig = plt.figure()
ax = fig.add_subplot(1,1,1,
                     projection=ccrs.PlateCarree()
                     )
ax.set_extent(
    [lons[0], lons[-1], lats[0], lats[-1]],
    crs=ccrs.PlateCarree()
)


# map.drawcoastlines(linewidth=0.2)
ax.add_feature(cfeature.COASTLINE, lw=0.2)
ax.add_feature(cfeature.BORDERS, linewidth=0.2)

conf = ax.contourf(
    lons, lats, da_result,
    levels = [20, 30, 40, 50, 60, 70, 80],
    cmap='coolwarm',
    zorder=1,
    extend='both'
    )


# mask ocean - but only above other data,
# should not mask this data, yet it does...
ax.add_feature(cartopy.feature.OCEAN, 
               color = '#DEFFFF',
               zorder=2)

fig.colorbar(conf, orientation='horizontal')

plt.savefig('images/test_percentile.png')




