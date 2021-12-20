import requests
from config import KEY
from haversine import haversine

def get_nearest(lat, lng):
    url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat}%2C{lng}&radius=1500&keyword=mcdonalds&key={KEY}'
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
