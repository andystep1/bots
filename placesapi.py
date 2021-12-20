import requests
from haversine import haversine

def get_nearest(lat, lng):
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=55.706238%2C37.596593&radius=1500&keyword=mcdonalds&key=AIzaSyCqktP2kqgQEB48wgygH7FeeAQNHOwLIdA"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    json = response.json()

    lat = [json['results'][i]['geometry']['location']['lat'] for i in range(len(json))]
    lng = [json['results'][i]['geometry']['location']['lng'] for i in range(len(json))]
    return [i for i in zip(lat, lng)]

def find_nearest(latlong, results_list):
    relist = [(haversine(latlong, i), i) for i in results_list]
    return sorted(relist)[0][1]

