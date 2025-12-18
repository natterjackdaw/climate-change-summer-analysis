import os
import numpy as np
import netCDF4 as nc
import xarray as xr


data_dir = f"{os.getcwd()}/data"
data_path = f"{data_dir}/summer_mean_2m_temperature_europe_1950-2025.nc"

ds = xr.open_dataset(data_path, engine="netcdf4")
# ds = nc.Dataset(data_path)
da = ds["t2m"].to_numpy()
print(type(da))
print(da.shape)

max_summer = da.max(axis=0)
print(max_summer.shape)
latest_year = da[-1,:,:]
print(latest_year)

diff = latest_year - max_summer
print(diff)

is_hottest = np.where(diff == 0, 1, None)
print(is_hottest)
