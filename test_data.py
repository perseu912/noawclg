from noawclg import get_noaa_data as gnd

data_noaa = gnd()

temp = data_noaa['tmp80m']

lon = data_noaa['lon']

lat = data_noaa['lat']
print(lat)