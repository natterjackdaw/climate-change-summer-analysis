import os

import xarray as xr


# Ask Xarray to not show data values by default
# xr.set_options(display_expand_data=False)

data_path = f"{os.getcwd()}/data"

ds_grib = xr.open_dataset(
    f"{data_path}/monthly_mean_2m_temperature_europe_195006-202508.grib", 
    engine="cfgrib"
)

print(ds_grib["time.year"])

# use group by