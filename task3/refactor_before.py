import json, os, sys, numpy, geopandas, paramiko, arcgis, fiona, sklearn, selenium, mojaPACZKA, math, functools, \
    tensorflow, pprint, pandas, copy, datetime
from requests import *


class mój_własny_Expcetion(Exception):
    pass


PlacKonesera = get('http://api.geonames.org/postalCodeLookupJSON?postalcode=03-736&country=PL&username=EMPTY')
kaliforniaKod = get('http://api.geonames.org/postalCodeLookupJSON?postalcode=90210&country=US&username=EMPTY')
ROMAkoddd = get('http://api.geonames.org/postalCodeLookupJSON?postalcode=00153&country=IT&username=EMPTY')
PARYŻ = get('http://api.geonames.org/postalCodeLookupJSON?postalcode=75000&country=FR&username=EMPTY')
monaco = get('http://api.geonames.org/postalCodeLookupJSON?postalcode=98000&country=MC&username=EMPTY')
PlacKonesera1 = PlacKonesera.json()
kaliforniaKod1 = kaliforniaKod.json()
ROMAkoddd1 = ROMAkoddd.json()
PARYŻ1 = PARYŻ.json()
monaco1 = monaco.json()
PlacKonesera2 = PlacKonesera1['postalcodes']
kaliforniaKod2 = kaliforniaKod1['postalcodes']
ROMAkoddd2 = ROMAkoddd1['postalcodes']
PARYŻ2 = PARYŻ1['postalcodes']
monaco2 = monaco1['postalcodes']
koneser_lista = []
for e in PlacKonesera2:
    koneser_lista.append(e['placeName'])
    koneser_lista.append(e['adminName1'])
    koneser_lista.append(e['postalcode'])
    koneser_lista.append(e['countryCode'])
    koneser_lista.append(e['lat'])
    koneser_lista.append(e['lng'])
kalifornia_lista = []
for e in kaliforniaKod2:
    kalifornia_lista.append(e['placeName'])
    kalifornia_lista.append(e['adminName1'])
    kalifornia_lista.append(e['postalcode'])
    kalifornia_lista.append(e['countryCode'])
    kalifornia_lista.append(e['lat'])
    kalifornia_lista.append(e['lng'])
romalista = []
for e in ROMAkoddd2:
    romalista.append(e['placeName'])
    romalista.append(e['adminName1'])
    romalista.append(e['postalcode'])
    romalista.append(e['countryCode'])
    romalista.append(e['lat'])
    romalista.append(e['lng'])
paryz_lista = []
for e in PARYŻ2:
    paryz_lista.append(e['placeName'])
    paryz_lista.append(e['adminName1'])
    paryz_lista.append(e['postalcode'])
    paryz_lista.append(e['countryCode'])
    paryz_lista.append(e['lat'])
    paryz_lista.append(e['lng'])
monacoLista = []
for e in monaco2:
    monacoLista.append(e['placeName'])
    monacoLista.append(e['adminName1'])
    monacoLista.append(e['postalcode'])
    monacoLista.append(e['countryCode'])
    monacoLista.append(e['lat'])
    monacoLista.append(e['lng'])
import pandas as panda

try:
    for f in ['csv', 'xlsx']:
        koneserpandas = panda.DataFrame([koneser_lista],
                                        columns=['placeName', 'adminName1', 'postalcode', 'countryCode', 'lat', 'lng'])
        kaliforniapandas = panda.DataFrame([kalifornia_lista],
                                           columns=['placeName', 'adminName1', 'postalcode', 'countryCode', 'lat',
                                                    'lng'])
        rzympandas = panda.DataFrame([romalista],
                                     columns=['placeName', 'adminName1', 'postalcode', 'countryCode', 'lat', 'lng'])
        prayzpandas = panda.DataFrame([paryz_lista],
                                      columns=['placeName', 'adminName1', 'postalcode', 'countryCode', 'lat', 'lng'])
        monacopandas = panda.DataFrame([monacoLista],
                                       columns=['placeName', 'adminName1', 'postalcode', 'countryCode', 'lat', 'lng'])
        ostateczny = koneserpandas.append(
            [kaliforniapandas.append(rzympandas.append(prayzpandas.append(monacopandas)))])
        import os

        my_path = 'D:\dump_folder'
        if f == 'csv':
            ostateczny.to_csv(my_path + os.sep + 'wynikowe_dane' + os.sep + 'format_csv' + os.sep + 'wyniki.csv')
        else:
            ostateczny.to_excel(my_path + os.sep + 'wynikowe_dane' + os.sep + 'format_xlsx' + os.sep + 'wyniki.xlsx')
except mój_własny_Expcetion:
    pass
except:
    pass
print('UDAŁO SIĘ!')
