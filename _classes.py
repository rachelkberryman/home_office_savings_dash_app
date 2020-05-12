# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 10:21:11 2020

@author: PaulM
"""

# %% 00 Packages and directories

# =============================================================================
# 00.0 Official python packages
# =============================================================================
from _config import *

# %% Class


class RentCalculator:

    # City price dictionary
    cities = city_price_dict
    # Space requirement list
    space_types = space_dict

    # List of information needed for the upcoming methods
    def __init__(self, city, num_emply, space, days_home_office=0):
        self.city = city
        self.num_emply = num_emply
        self.space = space
        self.days_home_office = days_home_office
        self.rent = self.calculate_rent(self.city,
                                        self.num_emply,
                                        self.space)
        self.savings = self.home_office_savings(self.days_home_office,
                                                self.rent)

    def calculate_rent(self, city, num_emply, space):
        # Extract city
        rel_sqm_price = RentCalculator.cities[city]
        # Extract space type
        rel_space = RentCalculator.space_types[space]
        # Calculation of the rent
        return rel_sqm_price * rel_space * num_emply

    def home_office_savings(self, days_home_office, rent):
        saving_percent = days_home_office/5
        return rent * saving_percent
