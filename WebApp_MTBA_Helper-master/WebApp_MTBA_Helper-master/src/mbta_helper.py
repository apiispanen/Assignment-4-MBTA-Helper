import urllib.request   # urlencode function
import json
import requests
from pprint import pprint



# Useful URLs (you need to add the appropriate parameters for your requests)



# A little bit of scaffolding if you want to use it

def latlong(address):
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {'address':address,'key':'AIzaSyDBBSBR4v4siDHgTi3cydOdgBljPoo9XAo'}
    a = requests.get(url,params=params)
    c = a.status_code
    r = a.json()['results'][0]['geometry']['location']
    latitude = r['lat']
    longitude = r['lng']
    return [latitude, longitude] 
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    

def get_nearest_station(lnl):
    url = "http://realtime.mbta.com/developer/api/v2/stopsbylocation"
    lat = lnl[0]
    lng = lnl[1] 
    paras = {'api_key':'wX9NwuHnZU2ToO7GmGR9uw', 'lat':lat, 'lon': lng, 'format':'json'}
    a = requests.get(url, params=paras)
    b = a.json()
    name = b['stop'][0]['stop_name']
    distance = b['stop'][0]['distance']
    return (name, distance)
    
    
    """
    Given latitude and longitude strings, return a (station_name, distance)
    tuple for the nearest MBTA station to the given coordinates.
    See http://realtime.mbta.com/Portal/Home/Documents for URL
    formatting requirements for the 'stopsbylocation' API in 'MBTA-realtime API v2 Documentation'.
    """
    
def find_stop_near(place_name):
    specs = latlong(place_name)
    # print(specs)
    # print(get_nearest_station(specs))
    return 'The nearest stop to {} is {} by {} miles'.format(place_name, get_nearest_station(specs)[0],  get_nearest_station(specs)[1])

