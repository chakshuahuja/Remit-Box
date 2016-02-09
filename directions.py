import json, urllib
from urllib import urlencode
import googlemaps
from BeautifulSoup import BeautifulSoup 

start = "Bridgewater, Sa, Australia"
finish = "Stirling, SA, Australia"
url = 'http://maps.googleapis.com/maps/api/directions/json?%s' % urlencode((
('origin', start),
('destination', finish)
))
ur = urllib.urlopen(url)
result = json.load(ur)
for i in range (0, len (result['routes'][0]['legs'][0]['steps'])):
    j = result['routes'][0]['legs'][0]['steps'][i]['html_instructions']
    soup = BeautifulSoup(j)
    print soup
