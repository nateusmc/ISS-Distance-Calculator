import requests
from calc import calc_distance

# ISS Location pulled from API
issInfo = requests.get('http://api.open-notify.org/iss-now.json').json()
issLat = issInfo['iss_position']['latitude']
issLon = issInfo['iss_position']['longitude']
issLocation = float(issLat), float(issLon)

# User's Current Location Based on IP
myPosInfo = requests.get('http://ip-api.com/json').json()
myLocationLat = float(myPosInfo['lat'])
myLocationLon = float(myPosInfo['lon'])
myLocation = myLocationLat, myLocationLon

# Print Locations
print('The ISS\'s Position is: ', issLocation)
print('Your location is: ', myLocation)

# Calculate distance of ISS from my location
distance = calc_distance(myLocationLat, issLat, myLocationLon, issLon)
print('The ISS is', round(distance, 2), 'km', 'from your current location')
