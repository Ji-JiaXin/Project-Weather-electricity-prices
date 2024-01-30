#execuce jinych - budeme volat funkce sem
import os
import pandas as pd

# Path to the new working directory
new_directory = "C:/Users/Sedláček/pr/Project-Weather-electricity-prices/Data"

# Changing the current working directory
os.chdir(new_directory)

from Weather_data_preparation import *
from Data_merge import *

#new_directory = "C:/Users/Sedláček/pr/Project-Weather-electricity-prices/Processing_and_graphs"

# Changing the current working directory
#os.chdir(new_directory)

#from Searching_sqr_diff import find_similar_temperature_periods