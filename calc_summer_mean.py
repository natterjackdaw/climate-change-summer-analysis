import os

import xarray as xr


# Ask Xarray to not show data values by default
# xr.set_options(display_expand_data=False)

data_dir = f"{os.getcwd()}/data"
data_path = f"{data_dir}/monthly_mean_2m_temperature_europe_195006-202508.grib"

print(f"Reading {data_path}")
ds_grib = xr.open_dataset(
    data_path, engine="cfgrib"
)

# mean summer temperature, not monthly mean
ds_summer = ds_grib.groupby('time.year').mean('time')

