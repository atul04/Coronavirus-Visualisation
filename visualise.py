# @Author: Atul Sahay <atul>
# @Date:   2020-03-16T23:28:22+05:30
# @Email:  atulsahay01@gmail.com
# @Last modified by:   atul
# @Last modified time: 2020-03-17T01:24:30+05:30


import pandas as pd
import folium
import locale
from folium import plugins
from folium.plugins import HeatMap
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="specify_your_app_name_here")

data = pd.read_csv("CoronaCases.csv")
print(data.head())

locations = [[35.000074, 104.999927], [42.6384261, 12.674297], [32.6475314, 54.5643516], [39.3262345, -4.8380649], [36.638392, 127.6961188], [51.0834196, 10.4234469], [46.603354, 1.8883335], [39.7837304, -100.4458825], [46.7985624, 8.2319736], [54.7023545, -3.2765753], [52.5001698, 5.7480821], [60.5000209, 9.0999715], [59.6749712, 14.5208584], [50.6402809, 4.6667145], [47.2000338, 13.199959], [55.670249, 10.3333283], [36.5748441, 139.2394179], [53.8953584, 27.5554078], [4.5693754, 102.2656823], [25.3336984, 51.2295295], [-24.7761086, 134.755], [61.0666922, -107.9917071], [38.9953683, 21.9877132], [40.0332629, -7.8896263], [49.8167003, 15.4749544], [63.2467777, 25.9209164], [31.5313113, 34.8667654], [45.8133113, 14.4808369], [1.357107, 103.8194992], [26.1551249, 50.5344606], [58.7523778, 25.3319078], [-10.3333333, -53.2], [64.9841821, -18.1059013], [52.865196, -7.9794599], [45.9852129, 24.6859225], [52.215933, 19.134422], [22.2793278, 114.1628131], [-31.7613365, -71.3187697], [26.2540493, 29.2675469], [14.8971921, 100.83273], [12.7503486, 122.7312101], [30.3308401, 71.247499], [-2.4833826, 117.8902853], [22.3511148, 78.6677428], [33.0955793, 44.1749775], [29.2733964, 47.4979476], [25.6242618, 42.3528328], [43.9458623, 12.458306], [33.8750629, 35.843409], [49.4871968, 31.2718321], [64.6863136, 97.7453061], [-6.8699697, -75.0458515], [49.8158683, 6.1296751], [48.7411522, 19.4528646], [23.9739374, 120.9820179], [-28.8166236, 24.991639], [42.6073975, 25.4856617], [13.2904027, 108.4265113], [-1.3397668, -79.3666965], [45.5643442, 17.0118954], [44.024322850000004, 21.07657433209902], [-34.9964963, -64.9672817], [8.559559, -81.1308434], [28.0000272, 2.9999825], [4.4137155, 114.5653908], [2.8894434, -73.783892], [19.4326296, -99.1331785], [41.000028, 19.9999619], [47.1817585, 19.5060937], [31.94696655, 35.27386547291496], [53.4250605, 27.6971358], [10.2735633, -84.0739102], [56.8406494, 24.7537645], [32.3293809, -83.1137366], [34.9823018, 33.1451285], [40.7696272, 44.6736646], [35.8885993, 14.4476911], [31.1728205, -7.3362482], [7.5554942, 80.7137847], [40.3936294, 47.7872508], [14.4750607, -14.4529612], [44.3053476, 17.5961467], [47.2879608, 28.5670941], [21.0000287, 57.0036901], [33.7680065, 66.2385139], [33.8439408, 9.400138], [31.1667049, 36.941628], [41.6171214, 21.7168387], [62.0448724, -7.0322972], [38.9597594, 34.9249653], [55.3500003, 23.7499997], [8.0018709, -66.1109318], [12.0753083, -1.6880314], [18.1152958, -77.1598454610168], [14.6113732, -60.9620777], [42.5407167, 1.5732033], [4.7064352, 73.3287853], [13.5066394, 104.869423], [22.1757605, 113.5514142], [19.0974031, -70.3028026], [-17.0568696, -64.9912286], [4.0039882, -52.999998], [47.2286086, 65.2093197], [-21.1309332, 55.5265771], [-41.5000831, 172.8344077], [24.4768598, 90.2932299], [-23.3165935, -58.1693445], [-32.8755548, -56.0201525], [41.32373, 63.9528098], [4.8417097, -58.6416891], [47.1416307, 9.5531527], [43.7323492, 7.4276832], [60.6167942, -145.7996671], [8.0300284, -1.0800271], [16.2490067, -61.5650444], [15.2572432, -86.0755145], [49.4871968, 31.2718321], [10.2116702, 38.6521203], [18.2214149, -66.41328179513847], [-1.9646631, 30.0644358], [4.6125522, 13.1535811], [7.9897371, -5.5679458], [23.0131338, -80.8328748], [10.8677845, -60.9821067], [-16.03442485, -146.0490931059517], [13.450125700000001, 144.75755102972062], [1.4419683, 38.4313975], [17.9036287, -62.811568843006896], [-4.6574977, 55.4540146], [15.6356088, -89.8988087], [9.6000359, 7.9999721], [12.5013629, -69.9618475], [12.1845, -68.9640875031406], [-4.0324901, 22.457478747924338], [-23.2335499, 17.3231107], [13.8250489, -60.975036], [48.5683066, 6.7539988], [19.5417212, -80.5667132], [14.5844444, 29.4917691], [28.1083929, 84.0917139], [17.2234721, -61.9554608], [24.7736546, -78.0000547], [9.5293472, 2.2584408], [27.549511, 90.5119273], [40.5250362, -81.0927234], [-0.7264327, 15.6419155], [1.613172, 10.5170357], [-0.8999695, 11.6899699], [36.10674695, -5.335277183483561], [77.6192349, -42.8125967], [10.7226226, -10.7083587], [41.90381485, 12.453152716779822], [5.7499721, -9.3658524], [20.2540382, -9.2399263], [-12.823048, 45.1520755], [46.8250388, 103.8499736], [12.90447, -61.2765569], [8.3676771, 49.083416], [4.1413025, -56.0771187], [-26.5624806, 31.3991317], [-6.5247123, 35.7878438], [8.7800265, 1.0199765], [17.789187, -64.7080574]]


# for country in data['Country']:
#     print(country)
#     location = geolocator.geocode(country)
#     locations.append([location.latitude, location.longitude])
# print(locations)

a = "8,880"
int(a.replace(',', ''))
totalCases = [int(i.replace(',', '')) for i in data['TotalCases']]
max_amount = max(totalCases)
print(max_amount)
normalize_radius = [ 10+i*30/max_amount for i in totalCases ]

data2plot = []

data['Country'].iloc[1]

for i in range(len(totalCases)):
    data2plot.append([locations[i][0], locations[i][1],totalCases[i]])

# m = folium.Map(location=(a,b), zoom_start=5)

m = folium.Map(location=[100, 0], zoom_start=3)

for i in range(len(locations)):
    folium.CircleMarker(location=locations[i],
    popup=data['Country'].iloc[i]+str("\n\n Total Cases = ")+str(totalCases[i])+str("\n Deaths = ")+str(data['TotalDeaths'].iloc[i]),
                            radius=normalize_radius[i],
                            fill_color="#3db7e4", # divvy color
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
m.save('index.html')
