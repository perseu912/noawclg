from noawclg import get_noaa_data as gnd

data_noaa = gnd()['tmp80m']

print(data_noaa)