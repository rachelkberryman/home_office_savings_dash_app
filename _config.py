# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 10:30:19 2020

@author: PaulM
"""

# %% 00 Packages and directories

# =============================================================================
# 00.0 Import Python packages
# =============================================================================
import pickle


# %% 01 Importing class required information

city_price_dict = pickle.load(open('assets' + "//city_price.p", "rb"))

space_dict = pickle.load(open('assets' + "//space_dict.p", "rb"))

# %% 02 Importing the colors

colors = ["#587B7F", "#1E2019", "#384032", "#8DAB7F", "#CFEE9E",
          "#C6D4FF", "#7A82AB", "#12664F", "#2DC2BD", "#283D3B",
          "#EDDDD4", "#C44536", "#772E25", "#DEE5E5", "#9DC5BB",
          "#17B890", "#082D0F"
          ]
