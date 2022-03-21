from osm import OSM
from publicTransport import PublicTransportAccessibility
import requests
# bhv 53.51500036203292, 8.603602165157444
lon = 8.603602165157444 # 8.6039883
lat = 53.51500036203292  # 52.51608

# TODO Get real value based on a metric radius
areaHeightRadius = 0.01 # 0.01
areaWidthRadius = 0.013 # 0.013

minLon = round(float(lon) - areaWidthRadius, 5)
maxLon = round(float(lon) + areaWidthRadius, 5)

minLat = round(float(lat) - areaHeightRadius, 5)
maxLat = round(float(lat) + areaHeightRadius, 5)

requestUrl = "https://overpass-api.de/api/map" 
requestsUrlParams = f"?bbox={minLon},{minLat},{maxLon},{maxLat}"

print(requestUrl + requestsUrlParams)

print("Downloading OSM-File...")
# TODO Check if banned from overpass-api 
r = requests.get(requestUrl + requestsUrlParams, headers={'Content-Type': 'application/xml'})
print("Done: Downloading OSM-File")



osm = OSM(r.text)
pta = PublicTransportAccessibility(osm)

print("Bus:" + str(pta.isBusAccessible()))
print("Tram:" + str(pta.isTramAccessible()))
print("Light Rail:" + str(pta.isLightRailAccessible()))
print("Subway:" + str(pta.isSubwayAccessible()))
print("Train:" + str(pta.isTrainAccessible()))
print("Monorail:" + str(pta.isMonorailAccessible()))