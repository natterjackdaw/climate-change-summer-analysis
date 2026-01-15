import os
from typing import List

# climate data download library
import cdsapi


full_map = [90, -180, -90, 180]

def download_grib_monthly_mean_data(
        v: str = "2m_temperature",
        min_month: int = 1,
        max_month: int = 12,
        min_year: int = 1950,
        max_year: int = 2025,
        lat_lon_area: List[int] = full_map,
        area_desc: str = ''
) -> None:
    """
    Download monthly mean re-analysis for one variable.
    
    :param v: Name of the variable you want to download
    :type v: str
    :param min_month: Earliest month in the year to download for
    :type min_month: int
    :param max_month: Latest month in the year to download for
    :type max_month: int
    :param min_year: Earliest year to download
    :type min_year: int
    :param max_year: Last year to download
    :type max_year: int
    :param lat_lon_area: [N, W, S, E]
    :type lat_lon_area: List[int]
    :param area_desc: A string to put in file to describe area (default is empty)
    :type area_desc: str
    """

    months = [
         f"{m:02}" for m in range(min_month, max_month+1)
    ]
    min_month_str = months[0]
    max_month_str = months[-1]

    years = [
        str(year) for year in
        range(min_year, max_year + 1)
    ]


    client = cdsapi.Client()
    dataset = "reanalysis-era5-single-levels-monthly-means"

    data_dir = f"{os.getcwd()}/data"
    existing_files = os.listdir(data_dir)

    target = f"monthly_mean_{v}_{area_desc}_{min_year}{min_month_str}-{max_year}{max_month_str}.grib"
    target_path = f"{data_dir}/{target}"

    if target in existing_files:
        
        print(f"{target} already downloaded...")
    
    else:

        request = {
            "product_type": ["monthly_averaged_reanalysis"],
            "variable": [v],
            "year": years,
            "month": months,
            "time": ["00:00"],
            "data_format": "grib",
            "download_format": "unarchived",
            "area": lat_lon_area
            }

                
        print(f"Downloading to {target_path}...")
        client.retrieve(dataset, request, target_path)


if __name__ == "__main__":

    europe_area = [72, -25, 35, 65]

    download_grib_monthly_mean_data(
        min_year=1950,
        max_year=2025,
        min_month=6,
        max_month=8,
        lat_lon_area=europe_area,
        area_desc="europe"
    )