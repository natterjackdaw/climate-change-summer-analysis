import os

import xarray as xr


data_dir = f"{os.getcwd()}/data"

# future work: make these less manual
data_path = f"{data_dir}/monthly_mean_2m_temperature_europe_195006-202508.grib"
out_path = f"{data_dir}/summer_mean_2m_temperature_europe_1950-2025.nc"

print(f"Reading {data_path}")
ds_grib = xr.open_dataset(
    data_path, engine="cfgrib"
)

# mean summer temperature, not monthly mean
ds_summer = ds_grib.groupby('time.year').mean('time')

# save as netCDF
print(f"Saving summer means to {out_path}...")
ds_summer.to_netcdf(
    path=out_path,
    mode="a" # in case we add future years
)