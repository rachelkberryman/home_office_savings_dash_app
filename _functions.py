# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 07:59:14 2020

@author: PaulM
"""

# %%


def city_class_separator(data):
    """
    This function separates the city class and the name of the city

    Parameters
    ----------
    data : DataFrame
        This dataframe has the city and the city classification combined

    Returns
    -------
    city_class : list
        list of all the city classes
    city_name : list
        list of all the city names
    """
    # Removing tyep None
    data.dropna(inplace=True)
    data = data.str.rstrip()
    # Extracting city group
    city_class = [x[-1] for x in data.str.split(' ')]
    # Extracting city name
    city_name_list = [x[1:-1] for x in data.str.split(' ')]
    city_name = [" ".join(item) for item in city_name_list]
    # Returning city and classification
    return city_class, city_name

