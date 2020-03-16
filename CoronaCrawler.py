# @Author: Atul Sahay <atul>
# @Date:   2019-01-27T16:51:15+05:30
# @Email:  atulsahay01@gmail.com
# @Last modified by:   atul
# @Last modified time: 2020-03-17T01:20:52+05:30

import pandas as pd
import folium
import math
from folium import plugins
from folium.plugins import HeatMap
from geopy.geocoders import Nominatim

import time
import requests
import re
import numpy
import pandas as pd
from bs4 import BeautifulSoup
# import lxml.html

import csv

# ######### Need to wake up the webdriver

while(True):
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

    
    
    ### Visualisation Module ###
    geolocator = Nominatim(user_agent="specify_your_app_name_here")

    data = pd.read_csv("CoronaCases.csv")
    print(data.head())
    # data = data.convert_objects(convert_numeric=True).fillna(0)
    locations = {' China ': [35.000074, 104.999927], ' Italy ': [42.6384261, 12.674297], ' Iran ': [32.6475314, 54.5643516], ' Spain ': [39.3262345, -4.8380649], ' S. Korea ': [36.638392, 127.6961188], ' Germany ': [51.0834196, 10.4234469], ' France ': [46.603354, 1.8883335], ' USA ': [39.7837304, -100.4458825], ' Switzerland ': [46.7985624, 8.2319736], ' UK ': [54.7023545, -3.2765753], ' Netherlands ': [52.5001698, 5.7480821], ' Norway ': [60.5000209, 9.0999715], ' Sweden ': [59.6749712, 14.5208584], ' Belgium ': [50.6402809, 4.6667145], ' Austria ': [47.2000338, 13.199959], ' Denmark ': [55.670249, 10.3333283], ' Japan ': [36.5748441, 139.2394179], ' Diamond Princess ': [53.8953584, 27.5554078], ' Malaysia ': [4.5693754, 102.2656823], ' Qatar ': [25.3336984, 51.2295295], ' Canada ': [61.0666922, -107.9917071], ' Australia ': [-24.7761086, 134.755], ' Greece ': [38.9953683, 21.9877132], ' Czechia ': [49.8167003, 15.4749544], ' Portugal ': [40.0332629, -7.8896263], ' Israel ': [31.5313113, 34.8667654], ' Finland ': [63.2467777, 25.9209164], ' Slovenia ': [45.8133113, 14.4808369], ' Singapore ': [1.357107, 103.8194992], ' Brazil ': [-10.3333333, -53.2], ' Bahrain ': [26.1551249, 50.5344606], ' Estonia ': [58.7523778, 25.3319078], ' Iceland ': [64.9841821, -18.1059013], ' Pakistan ': [30.3308401, 71.247499], ' Ireland ': [52.865196, -7.9794599], ' Romania ': [45.9852129, 24.6859225], ' Poland ': [52.215933, 19.134422], ' Chile ': [-31.7613365, -71.3187697], ' Hong Kong ': [22.2793278, 114.1628131], ' Egypt ': [26.2540493, 29.2675469], ' Thailand ': [14.8971921, 100.83273], ' Philippines ': [12.7503486, 122.7312101], ' Indonesia ': [-2.4833826, 117.8902853], ' Iraq ': [33.0955793, 44.1749775], ' Saudi Arabia ': [25.6242618, 42.3528328], ' India ': [22.3511148, 78.6677428], ' Kuwait ': [29.2733964, 47.4979476], ' San Marino ': [43.9458623, 12.458306], ' Lebanon ': [33.8750629, 35.843409], ' UAE ': [49.4871968, 31.2718321], ' Russia ': [64.6863136, 97.7453061], ' Peru ': [-6.8699697, -75.0458515], ' Luxembourg ': [49.8158683, 6.1296751], ' Slovakia ': [48.7411522, 19.4528646], ' Taiwan ': [23.9739374, 120.9820179], ' South Africa ': [-28.8166236, 24.991639], ' Bulgaria ': [42.6073975, 25.4856617], ' Vietnam ': [13.2904027, 108.4265113], ' Algeria ': [28.0000272, 2.9999825], ' Ecuador ': [-1.3397668, -79.3666965], ' Croatia ': [45.5643442, 17.0118954], ' Serbia ': [44.024322850000004, 21.07657433209902], ' Argentina ': [-34.9964963, -64.9672817], ' Panama ': [8.559559, -81.1308434], ' Brunei ': [4.4137155, 114.5653908], ' Colombia ': [2.8894434, -73.783892], ' Mexico ': [19.4326296, -99.1331785], ' Albania ': [41.000028, 19.9999619], ' Cyprus ': [34.9823018, 33.1451285], ' Armenia ': [40.7696272, 44.6736646], ' Hungary ': [47.1817585, 19.5060937], ' Palestine ': [31.94696655, 35.27386547291496], ' Belarus ': [53.4250605, 27.6971358], ' Costa Rica ': [10.2735633, -84.0739102], ' Latvia ': [56.8406494, 24.7537645], ' Georgia ': [32.3293809, -83.1137366], ' Malta ': [35.8885993, 14.4476911], ' Morocco ': [31.1728205, -7.3362482], ' Moldova ': [47.2879608, 28.5670941], ' Sri Lanka ': [7.5554942, 80.7137847], ' Azerbaijan ': [40.3936294, 47.7872508], ' Bosnia and Herzegovina ': [44.3053476, 17.5961467], ' Senegal ': [14.4750607, -14.4529612], ' Oman ': [21.0000287, 57.0036901], ' Afghanistan ': [33.7680065, 66.2385139], ' Dominican Republic ': [19.0974031, -70.3028026], ' Tunisia ': [33.8439408, 9.400138], ' Jordan ': [31.1667049, 36.941628], ' North Macedonia ': [41.6171214, 21.7168387], ' Faeroe Islands ': [62.0448724, -7.0322972], ' Turkey ': [38.9597594, 34.9249653], ' Lithuania ': [55.3500003, 23.7499997], ' Venezuela ': [8.0018709, -66.1109318], ' Burkina Faso ': [12.0753083, -1.6880314], ' Jamaica ': [18.1152958, -77.1598454610168], ' Martinique ': [14.6113732, -60.9620777], ' Andorra ': [42.5407167, 1.5732033], ' Maldives ': [4.7064352, 73.3287853], ' Cambodia ': [13.5066394, 104.869423], ' Macao ': [22.1757605, 113.5514142], ' Bolivia ': [-17.0568696, -64.9912286], ' French Guiana ': [4.0039882, -52.999998], ' Kazakhstan ': [47.2286086, 65.2093197], ' Réunion ': [-21.1309332, 55.5265771], ' Guatemala ': [15.6356088, -89.8988087], ' New Zealand ': [-41.5000831, 172.8344077], ' Bangladesh ': [24.4768598, 90.2932299], ' Paraguay ': [-23.3165935, -58.1693445], ' Uruguay ': [-32.8755548, -56.0201525], ' Uzbekistan ': [41.32373, 63.9528098], ' Guyana ': [4.8417097, -58.6416891], ' Ukraine ': [49.4871968, 31.2718321], ' Liechtenstein ': [47.1416307, 9.5531527], ' Monaco ': [43.7323492, 7.4276832], ' Channel Islands ': [60.6167942, -145.7996671], ' Ghana ': [8.0300284, -1.0800271], ' Guadeloupe ': [16.2490067, -61.5650444], ' Honduras ': [15.2572432, -86.0755145], ' Ethiopia ': [10.2116702, 38.6521203], ' Puerto Rico ': [18.2214149, -66.41328179513847], ' Rwanda ': [-1.9646631, 30.0644358], ' Cameroon ': [4.6125522, 13.1535811], ' Ivory Coast ': [7.9897371, -5.5679458], ' Cuba ': [23.0131338, -80.8328748], ' Trinidad and Tobago ': [10.8677845, -60.9821067], ' French Polynesia ': [-16.03442485, -146.0490931059517], ' Gibraltar ': [36.10674695, -5.335277183483561], ' Guam ': [13.450125700000001, 144.75755102972062], ' Kenya ': [1.4419683, 38.4313975], ' St. Barth ': [17.9036287, -62.811568843006896], ' Seychelles ': [-4.6574977, 55.4540146], ' Nigeria ': [9.6000359, 7.9999721], ' Aruba ': [12.5013629, -69.9618475], ' Curaçao ': [12.1845, -68.9640875031406], ' DRC ': [-4.0324901, 22.457478747924338], ' Namibia ': [-23.2335499, 17.3231107], ' Saint Lucia ': [13.8250489, -60.975036], ' Saint Martin ': [48.5683066, 6.7539988], ' Cayman Islands ': [19.5417212, -80.5667132], ' Sudan ': [14.5844444, 29.4917691], ' Nepal ': [28.1083929, 84.0917139], ' Antigua and Barbuda ': [17.2234721, -61.9554608], ' Bahamas ': [24.7736546, -78.0000547], ' Benin ': [9.5293472, 2.2584408], ' Bhutan ': [27.549511, 90.5119273], ' CAR ': [40.5250362, -81.0927234], ' Congo ': [-0.7264327, 15.6419155], ' Equatorial Guinea ': [1.613172, 10.5170357], ' Gabon ': [-0.8999695, 11.6899699], ' Greenland ': [77.6192349, -42.8125967], ' Guinea ': [10.7226226, -10.7083587], ' Vatican City ': [41.90381485, 12.453152716779822], ' Liberia ': [5.7499721, -9.3658524], ' Mauritania ': [20.2540382, -9.2399263], ' Mayotte ': [-12.823048, 45.1520755], ' Mongolia ': [46.8250388, 103.8499736], ' St. Vincent Grenadines ': [12.90447, -61.2765569], ' Somalia ': [8.3676771, 49.083416], ' Suriname ': [4.1413025, -56.0771187], ' Eswatini ': [-26.5624806, 31.3991317], ' Tanzania ': [-6.5247123, 35.7878438], ' Togo ': [8.7800265, 1.0199765], ' U.S. Virgin Islands ': [17.789187, -64.7080574]}


    # for country in data['Country,Other']:
    #     print(country)
    #     location = geolocator.geocode(country)
    #     locations[country] = [location.latitude, location.longitude]
    #     time.sleep(1)
    # print(locations)


    a = "8,880"
    int(a.replace(',', ''))
    totalCases = [int(i.replace(',', '')) for i in data['TotalCases']]
    max_amount = max(totalCases)
    print(max_amount)
    normalize_radius = [ 0.01+3*math.log(i,(2)) for i in totalCases ]
    print(normalize_radius)
    data2plot = []
    print(data['TotalDeaths'])

    active = []
    for i in data['ActiveCases']:
        if(i == ' '):
            active.append(0)
        else:
            active.append(int(i.replace(',', '')))


    death = []
    for i in data['TotalDeaths']:
        if(i == ' '):
            death.append(0)
        else:
            death.append(int(i.replace(',', '')))


    recovered = []
    for i in data['TotalRecovered']:
        if(i == ' '):
            recovered.append(0)
        else:
            recovered.append(int(i.replace(',', '')))



    # for i in range(len(totalCases)):
    #     data2plot.append([locations[i][0], locations[i][1],totalCases[i]])

    # m = folium.Map(location=(a,b), zoom_start=5)

    m = folium.Map(location=[45, 0], zoom_start=2.5)

    # html="""
    #     <h1> This is a big popup</h1><br>
    #     With a few lines of code...
    #     <p>
    #     <code>
    #         from numpy import *<br>
    #         exp(-2*pi)
    #     </code>
    #     </p>
    #     """

    legend_html = '''
        <div style='width: 25rem; position: fixed; text-align: center;
        box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
        bottom: 0px; left: 0px; z-index:9999; background-color: white; padding: 5px;'>
            <div class='card-body'>
                <h5 class='card-title'>Total Cases</h5 style='margin: 2px'>
                <h3 class='text-warning' style='margin: 0px'>{}</h3>
                <table class="table table-striped" style='margin: 0px'>
                    <thead>
                    <tr>
                        <th>Active</th>
                        <th>Recovered</th>
                        <th>Death</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr>
                        <td class='text-primary'>{}</td>
                        <td class='text-success'>{}</td>
                        <td class='text-danger'>{}</td>
                    </tr>
                    </tbody>
                </table>
                <div class="progress" style='margin: 0px'>
                    <div class="progress-bar progress-bar-primary" role="progressbar" style="width:{}%">
                    </div>
                    <div class="progress-bar progress-bar-success" role="progressbar" style="width:{}%">
                    </div>
                    <div class="progress-bar progress-bar-danger" role="progressbar" style="width:{}%">
                    </div>
                </div> 
            </div>
        </div>
        '''.format(sum(totalCases),sum(active), sum(recovered), sum(death), sum(active) * 100/ sum(totalCases), sum(recovered) * 100/ sum(totalCases), sum(death) * 100/ sum(totalCases))

    for i in range(len(locations)):
        folium.CircleMarker(location=locations[data['Country,Other'].iloc[i]],
        tooltip=data['Country,Other'].iloc[i]+str("\n\nTotal Cases = ")+str(totalCases[i])+str("\n Deaths = ")+str(data['TotalDeaths'].iloc[i]),
                                radius=normalize_radius[i],
                                fill_color="#FF0000", # divvy color
                                stroke=False,
                            ).add_to(m)


    # folium.CircleMarker(locations,
    #                         radius=normalize_radius,
    #                         popup=data['Country'],
    #                         fill_color="#3db7e4", # divvy color
    #                        ).add_to(m)
    # hm_wide = HeatMap( data2plot,
    #                    min_opacity=0.2,
    #                    max_val=max_amount,
    #                    radius=17, blur=15,
    #                    max_zoom=1,
                    # )
    # m.add_child(hm_wide)
    m.get_root().html.add_child(folium.Element(legend_html))
    m.save('./public_html/covid-19/index.html')
    time.sleep(5 * 60)
