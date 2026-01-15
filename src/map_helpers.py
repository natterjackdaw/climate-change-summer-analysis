import numpy as np
from typing import List, Dict

# def rearrange_for_prime_meridian(
#     map_data: np.numpy,
#     lons: List,
#     axis: int = 1
# ) -> Dict:
#     '''
#     Re-arranges data so that it may be mapped with a focus on Europe or Africa 
#     (i.e., the starting point is not 0). Therefore, longitudes become between 
#     -180 and 180, rather than values within 0-360).
    
#     :param map_data: The data to be mapped on a plot.
#     :type map_data: np.numpy
#     :param lons: The latitudes represented by the data.
#     :type lons: List
#     :param axis: which axis of the data is the longitude, where first is 0.
#     :type axis: int
#     :default axis: 1 (which would be the longitudes in a 2D (lon,lat) array)
#     :return: The converted latitude and data.
#     :rtype: Dict
#     '''
#     lon_len_in_data = map_data.shape()[axis]
#     # check that the shape of array matches the length of the longitude points
#     if lon_len_in_data != len(lons):
#         error_explanation = f"""Looks like the longitude input does not match
#         the shape of the data.
#         Are you using the correct axis? {axis}
#         The data shape is {map_data.shape()} and so the longitude expected is 
#         {lon_len_in_data}.
#         """
#         raise ValueError(error_explanation)
    
    # need to know at what point longitude has a value above 180
    