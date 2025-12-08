import os

import xarray as xr


# Ask Xarray to not show data values by default
xr.set_options(display_expand_data=False)

data_path = f"{os.getcwd()}/data"

ds_grib = xr.open_dataset(f"{data_path}/2m_temperature_europe_195007_alltime.grib", 
                        engine="cfgrib")

ds_mean = ds_grib.mean(["time", "step"])

print(ds_mean)