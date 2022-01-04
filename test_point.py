from noawclg import get_noaa_data as gnd
data_noaa = gnd()

place = 'salvador BA'


data_noaa.plot_temperature_from_place(place=place)