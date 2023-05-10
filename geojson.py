# https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody
# www.py4e.org

# web services (chapter 13)

import urllib.request, urllib.parse, urllib.parse
import json
# serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?Ann+Arbor%2C+MI'
serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
# https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody/web-services-apis

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode({'address': address})
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved',len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('====Failure to Retrieve====')
        print(data)
        continue

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)