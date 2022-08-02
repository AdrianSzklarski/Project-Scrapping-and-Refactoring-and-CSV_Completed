"""
    A program to retrieve information from any store with a senior card service.

    Input data:     URL of the store, cheakbox selection
    Output data:    CSV file with specific data

    Attention:
    module "connect_to_site" has been added to .gitignore, if it needs the code
    send a request to the author.
"""

import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from modul.connect import connect_to_site


driverPath = r'/home/adrian/Pulpit/Zadania_rekrutacyjne/Zadania/folder_task_2/webdrivers/chromedriver'
url = 'https://www.carrefour.pl/sklepy?must=seniorCard&should=carrefour%2Cmarket%2Cexpress%2CexpressConvenience%2Cglobi%2Csupeco'
savePath = r'/home/adrian/Pulpit/Portfolio na GITHUB/Na GitHub/Project - Scrappin and Refactoring and CSV/task2/task2.csv'


def get_shop_address():
    ''' Downloading store addresses from the website '''
    addressDivs = driver.find_elements(By.CLASS_NAME, 'jss277')
    addresses = []
    for div in addressDivs:
        address = div.find_element(By.TAG_NAME, 'p').text.replace('\n', ' ')
        addresses.append(address)
    return addresses


def get_shop_names():
    ''' Downloading store names from the website '''
    name_elements = driver.find_elements(By.CLASS_NAME, 'jss148')
    names = []
    for name in name_elements[:-7]:
        names.append(name.text)
    return names


def save_csv(data, path):
    ''' Saving data to a CSV file '''
    try:
        with open(path, 'a', newline="", encoding='UTF-8') as csvfile:
            writer = csv.writer(csvfile)
            if csvfile.tell() == 0:
                writer.writerow(['full_store_name', 'full_store_address'])
            writer.writerows(data)
    except:
        return False
    return True


with connect_to_site(driverPath, url) as driver:
    ''' Connection to Selenium driver '''

    # Acceptance of Cookies
    button = driver.find_element(
        By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
    button.click()

    # Downloading data from all tabs
    input_box = driver.find_element(By.CLASS_NAME, 'jss287')

    for page in range(1, 17):

        adresses = get_shop_address()
        names = get_shop_names()

        shops = list(zip(names, adresses))

        saved = save_csv(shops, savePath)
        if saved:
            input_box.send_keys(Keys.BACK_SPACE)
            input_box.send_keys(page)
            input_box.send_keys(Keys.ENTER)
            print(f'Save is correct number page {page}')
        else:
            print(f'Save is wrong number page {page}')
