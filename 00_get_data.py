import os
from typing import List

# climate data download library
import cdsapi

full_map = [90, -180, -90, 180]

summer_days_dict = {
    "06": 30,
    "07": 31,
    "08": 31
}

max_days = [
    "01", "02", "03",
    "04", "05", "06",
    "07", "08", "09",
    "10", "11", "12",
    "13", "14", "15",
    "16", "17", "18",
    "19", "20", "21",
    "22", "23", "24",
    "25", "26", "27",
    "28", "29", "30",
    "31"
]

def download_grib_summer_data(
        v: str = "2m_temperature",
        min_year: int = 1950,
        max_year: int = 2025,
        lat_lon_area: List[int] = full_map,
        area_desc: str = '',
        check_output: bool = False
) -> None:
    """
    Docstring for download_grib_data, one variable at a time.
    Loops through years and months.
    
    :param v: Which variable do you want to download using API
    :type v: str
    :param min_year: First year of data to download
    :type min_year: int
    :param max_year: Final year of data to download (inclusive)
    :type max_year: int
    :param months: Which months to download
    :type months: List[str]
    :param lat_lon_area: A list of 4 numbers - min latitude, 
    min longitude, max latitude, max longitude
    :type lat_lon_area: List[int]
    :param check_output: If True, it will not download data, just
    print the instructions
    :type check_output: bool
    """    

    months = summer_days_dict.keys()
    years = [
        str(year) for year in
        range(min_year, max_year + 1)
    ]

    dataset = "reanalysis-era5-land"

    client = cdsapi.Client()
    data_dir = f"{os.getcwd()}/data"
    existing_files = os.listdir(data_dir)

    for yyyy in years:
        for mm in months:

            target = f"{v}_{area_desc}_{yyyy}{mm}_alltime.grib"

            last_day = summer_days_dict[mm]
            days = max_days[:last_day]

            if target in existing_files:
                print(f"{target} already downloaded...")
                continue

            print(f"Starting API for {target}...")

            request = {
                "variable": [v],
                "year": yyyy,
                "month": mm,
                "day": days,
                "time": [
                    "00:00", "01:00", "02:00",
                    "03:00", "04:00", "05:00",
                    "06:00", "07:00", "08:00",
                    "09:00", "10:00", "11:00",
                    "12:00", "13:00", "14:00",
                    "15:00", "16:00", "17:00",
                    "18:00", "19:00", "20:00",
                    "21:00", "22:00", "23:00"
                ],
                "data_format": "grib",
                "download_format": "unarchived",
                "area": lat_lon_area
            }

            target_path = f"{data_dir}/{target}"

            print(f"Downloading {yyyy}-{mm} data")
            print(f"into {target_path}")

            if check_output == True:

                print(request)

            else:
                
                print("Downloading...")
                client.retrieve(dataset, request, target_path)#.download()

            print()


if __name__ == "__main__":

    europe_area = [25, -25, 72, 65]
    summer_months = ["06", "07", "08"]

    download_grib_summer_data(
        min_year=1950,
        max_year=1951,
        lat_lon_area=europe_area,
        area_desc="europe",
        check_output=False
    )