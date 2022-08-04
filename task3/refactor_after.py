import pandas as pd
import os
from requests import get

USERNAME = 'Login'


# REST APi processing function
def get_place_info(postalCode, country, username=USERNAME):
    r = get(
        f'http://api.geonames.org/postalCodeLookupJSON?postalcode={postalCode}&country={country}&username={username}')
    content = r.json()
    try:
        placeDict = content['postalcodes'][0]
    except IndexError:
        return {'error': 'Invalid argument. Try different postalCode, country or username.'}
    else:
        placeInfo = {
            'name': placeDict['placeName'],
            'adminName': placeDict['adminName1'],
            'postalCode': placeDict['postalcode'],
            'countryCode': placeDict['countryCode'],
            'lat': placeDict['lat'],
            'lng': placeDict['lng'],
        }
        return placeInfo


# Downloading and processing data from the API
warsawInfo = get_place_info('03-736', 'pl')  # koneser
californiaInfo = get_place_info('90210', 'US')
romeInfo = get_place_info('00153', 'IT')
parisInfo = get_place_info('75000', 'FR')
monacoInfo = get_place_info('98000', 'MC')

# Preparing data to create a table
placesInfo = list(zip(warsawInfo.values(), californiaInfo.values(),
                      romeInfo.values(), parisInfo.values(), monacoInfo.values()))
columns = [
    'placeName', 'adminName1', 'postalcode', 'countryCode', 'lat', 'lng']

# Creating a table and inverting it
infoFramed = pd.DataFrame(placesInfo, index=columns).transpose()

resultFolder = r'/home/adrian/Pulpit/Portfolio na GITHUB/Na GitHub/Project - Scrappin and Refactoring and CSV/task3'

# Export to CSV and Excel
try:
    infoFramed.to_csv(os.path.join(resultFolder, 'result.csv'))
    infoFramed.to_excel(os.path.join(resultFolder, 'result.xlsx'))
except FileNotFoundError as e:
    print(f'Invalid path: {e}')
