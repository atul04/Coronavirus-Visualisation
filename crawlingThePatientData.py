# @Author: Atul Sahay <atul>
# @Date:   2020-04-13T13:21:33+05:30
# @Email:  atulsahay01@gmail.com
# @Last modified by:   atul
# @Last modified time: 2020-04-13T14:06:40+05:30
import json
from urllib.request import urlopen
from geopy.geocoders import Nominatim
import numpy as np
import time

def insertData(districtMap,state,district):
    print(state,district)
    if((state,district) in districtMap):
        districtMap[(state,district)]['patientCount'] +=1
    else:
        time.sleep(4)
        location  = geolocator.geocode(district)
        (lat,lon) = [location.latitude, location.longitude]
        districtMap[(state,district)] = {"location":(lat,lon),"patientCount":1}
    print(districtMap[(state,district)])
def get(url, object_hook=None):
    with urlopen(url) as resource:  # 'with' is important to close the resource after use
        return json.load(resource, object_hook=object_hook)

data = get(url='https://api.rootnet.in/covid19-in/unofficial/covid19india.org')
print(len(data['data']['rawPatientData']))
print(data['data']['rawPatientData'][2]['district'])

districtMap ={}

geolocator = Nominatim(user_agent="specify_your_app_name_here")

for i in range(len(data['data']['rawPatientData'])):
    insertData(districtMap,data['data']['rawPatientData'][i]['state'],data['data']['rawPatientData'][i]['district'])

np.save('patientData.npy', districtMap)

with open("CoronaPatientData.csv",mode='w') as file:
    writer = csv.writer(file,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['State','District','Latitude','Longitude','PatientCount'])
    for item in districtMap.keys():
        row = []
        row.append(item[0])
        row.append(item[1])
        row.append(districtMap[item]['location'][0])
        row.append(districtMap[item]['location'][1])
        row.append(districtMap[item]['patientCount'])
        writer.writerow(row)
