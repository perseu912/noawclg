
<h1 align='center'>NOAWClg</h1>
<p align='center'>

<br/>
<a href="https://github.com/perseu912"><img title="Autor" src="https://img.shields.io/badge/Autor-reinan_br-blue.svg?style=for-the-badge&logo=github"></a>
<!-- <br/>
<a href='http://dgp.cnpq.br/dgp/espelhogrupo/0180330616769073'><img src='https://shields.io/badge/cnpq-grupo_de_fisica_computacional_ifsertao--pe-blueviolet?logo=appveyor&style=for-the-badge'></a> -->

<p align='center'>
<!-- github dados --
<!-- sites de pacotes -->
<a href='https://pypi.org/project/noaawc/'><img src='https://img.shields.io/pypi/v/noawclg'></a>
<a href='#'><img src='https://img.shields.io/pypi/wheel/noawclg'></a>
<a href='#'><img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/noawclg"></a>
<img alt="PyPI - License" src="https://img.shields.io/pypi/l/noawclg">
<br/>
<!-- outros premios e analises -->
<!-- <a href='#'><img alt="CodeFactor Grade" src="https://img.shields.io/codefactor/grade/github/perseu912/noawclg?logo=codefactor">
</a> -->
<!-- redes sociais -->
<a href='https://instagram.com/gpftc_ifsertao/'><img src='https://shields.io/badge/insta-gpftc_ifsertao-darkviolet?logo=instagram&style=flat'></a>
<a href='https://discord.gg/pFZP86gvEm'><img src='https://img.shields.io/discord/856582838467952680.svg?label=discord&logo=discord'></a>

</p>
</p>
<p align='center'> <b>Library for getting  the world data climate from the data noaa/nasa</b></p>
<hr/>

## Instalation

```sh
$ pip3 install noawcgl -U
```
note: netcdf=1.5.7 | xarray=0.20.1
## Examples
### getting data
<br>

#### from a point
getting the data:
```py
from noawclg import get_noaa_data as gnd

point = (-9.41,-40.5)

data = gnd.get_data_from_point(point)

# a example for the surface temperature
data = {'time':data['time'],'data':data['tmpsfc']}

print(data)
```

```sh
{'time': <xarray.IndexVariable 'time' (time: 129)>
array(['2022-01-01T00:00:00.000000000', '2022-01-01T03:00:00.000000000',
       '2022-01-01T06:00:00.000000000', '2022-01-01T09:00:00.000000000',
       '2022-01-01T12:00:00.000000000', 
...
```

### keys
```py
>>> from noawclg import get_noaa_data as  gnd

>>> gnd().get_noaa_keys()


{'time': 'time', 
'lev': 'altitude', 
'lat': 'latitude', 
'lon': 'longitude', 
'absvprs': '** (1000 975 950 925 900.. 10 7 4 2 1) absolute vorticity [1/s] ',
 'no4lftxsfc': '** surface best (4 layer) lifted index [k] ', 
 'acpcpsfc': '** surface convective precipitation [kg/m^2] ', 
 'albdosfc': '** surface albedo [%] ',
  'apcpsfc': '** surface total precipitation [kg/m^2] ', 
  'capesfc': '** surface convective available potential energy [j/kg] ', 
...
```

### example plot wind
```py
from noawclg.main import get_noaa_data as gnd
data_noaa = gnd(gfs='1p00')#,url_data='https://nomads.ncep.noaa.gov/dods/gfs_1p00/gfs20220108/gfs_1p00_00z')

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

```
result:
<img src='plot_wind100m.png'>
