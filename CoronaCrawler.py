# @Author: Atul Sahay <atul>
# @Date:   2019-01-27T16:51:15+05:30
# @Email:  atulsahay01@gmail.com
# @Last modified by:   atul
# @Last modified time: 2020-03-17T01:20:52+05:30



import time
import requests
import requests
from urllib.parse import quote_plus
import re
import numpy
import pandas as pd
from bs4 import BeautifulSoup
# import lxml.html

import csv

# ######### Need to wake up the webdriver
# path = 'geckodriver-v0.23.0-linux64/geckodriver'

# profile = webdriver.FirefoxProfile()
# profile.set_preference("webdriver.load.strategy", "unstable")
# profile.update_preferences()

# driver = webdriver.Firefox(firefox_binary=FirefoxBinary(),executable_path=path,firefox_profile=profile)
# t = time.time()
# driver.set_page_load_timeout(100)

# driver.get("https://www.worldometers.info/coronavirus/")

sauce = requests.get("https://www.worldometers.info/coronavirus/")


soup = BeautifulSoup(sauce.content, "html.parser")
# tree = lxml.html.fromstring(sauce.content)

tableContent =  soup.find('table', { 'id' : 'main_table_countries' })

thead = tableContent.find('thead')
# print(thead)
headers = []
for row in thead.findAll("tr"):
    for header in row.findAll("th"):
        headers.append(header.getText())
print(headers)
tbody = tableContent.find('tbody')
rows = []
for row in tbody.findAll("tr"):
    rowContent = []
    for cells in row.findAll("td"):
        rowContent.append(cells.getText())
    rows.append(rowContent)
for i in rows:
    print(i)
# Writing to the csv files ( particularly 2 READ and UNREAD )
with open("CoronaCases.csv",mode='w') as file:
    writer = csv.writer(file,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
    writer.writerow(headers)
    for row in rows:
        writer.writerow(row)
# print(tbody)


time.sleep(3)
