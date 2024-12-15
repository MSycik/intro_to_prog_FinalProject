import pandas as pd
from Regions import Region
from Continents import Continent
from menu import run_menu
from main import data

region_data = Region(data)
continent_data = Continent(data)

run_menu(region_data, continent_data)

