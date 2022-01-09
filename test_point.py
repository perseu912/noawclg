from noawclg.main import get_noaa_data as gnd
data_noaa = gnd(gfs='1p00',date='20220109',url_data='https://nomads.ncep.noaa.gov/dods/gfs_1p00/gfs20220108/gfs_1p00_00z')

place = 'juazeiro BA'
print(data_noaa.get_noaa_keys())


# ## rain's (mm)
# def fmt(data): return data* 100_000
# data_noaa.plot_data_from_place(place=place,path_file='plot_ch1.png',
#                                title='Previsão de Chuvas\nPetrolina-PE/Juazeiro-BA',
#                                 ylabel='mm',fmt_data=fmt,key_noaa='prateavesfc')



## temperature (ºC)
def fmt_t(data): return data
data_noaa.plot_data_from_place(place=place,path_file='plot_wind100m.png',
                               title='Velocidade dos Ventos\nPetrolina-PE/Juazeiro-BA',
                                ylabel='m/s',fmt_data=fmt_t,key_noaa='vgrdmwl')
