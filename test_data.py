from noawclg import get_noaa_data as gnd

data_noaa = gnd()

temp = data_noaa['tmp80m']

print(len(temp.to_pandas()))