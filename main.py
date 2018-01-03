import requests
from calc import calc_distance

# ISS Location pulled from API
issInfo = requests.get('http://api.open-notify.org/iss-now.json').json()
issInfo = requests.get('http://api.open-notify.org/iss-now.json').json()
issLat = float(issInfo['iss_position']['latitude'])
issLon = float(issInfo['iss_position']['longitude'])
issLocation = issLat, issLon

# User's Current Location Based on IP
myPosInfo = requests.get('http://ip-api.com/json').json()
myLocationLat = myPosInfo['lat']
myLocationLon = myPosInfo['lon']
myLocation = myLocationLat, myLocationLon

# Print Current ISS Locations
print('The ISS\'s Current Position is: ', issLocation)
print('')

# Calculate distance of ISS from my location
distance = calc_distance(myLocationLat, issLat, myLocationLon, issLon)
print('Distance from ISS according to your current location:')
print('The ISS is', round(distance, 0), 'km from your current location')

print('')
print('Distance from ISS according to each crew members Hometown on Expedition 54:')
print('')

# Acaba's Hometown Location
acabaLat = 33.836636
acabaLon = -117.914221

# Calculate distance of ISS from Acaba's Hometown
distance = calc_distance(acabaLat, issLat, acabaLon, issLon)
print("The ISS is", round(distance, 0), "km from Joseph M. Acaba's Hometown of Anaheim, California")

# Hei's Hometown Location
heiLat = 38.882412
heiLon = -77.173007

# Calculate distance of ISS from Hei's Hometown
distance = calc_distance(heiLat, issLat, heiLon, issLon)
print("The ISS is", round(distance, 0), "km from Mark T. Vande Hei's Hometown of Falls Church, Virginia")

# Tingle's Hometown Location
tingleLat = 42.180009
tingleLon = -71.054176

# Calculate distance of ISS from Tingle's Hometown
distance = calc_distance(tingleLat, issLat, tingleLon, issLon)
print("The ISS is", round(distance, 0), "km from Scott D. Tingle's Hometown of Randolph, Massachusetts")

# Alexandrovich's Hometown Location
alexandrovichLat = 52.967776
alexandrovichLon = 36.059538

# Calculate distance of ISS from Alexandrovich's Hometown
distance = calc_distance(alexandrovichLat, issLat, alexandrovichLon, issLon)
print("The ISS is", round(distance, 0), "km from Alexander Alexandrovich's Hometown of Orel, Russia")

# Nikolaevich's Hometown Location
nikolaevichLat = 53.456705
nikolaevichLon = 35.185575

# Calculate distance of ISS from Nikolaevich's Hometown
distance = calc_distance(nikolaevichLat, issLat, nikolaevichLon, issLon)
print("The ISS is", round(distance, 0), "km from Anton Nikolaevich's Hometown of Sevastopol, Russia")

# Kanai's Hometown Location
kanaiLat = 35.620887
kanaiLon = 140.107225

# Calculate distance of ISS from Kanai's Hometown
distance = calc_distance(kanaiLat, issLat, kanaiLon, issLon)
print("The ISS is", round(distance, 0), "km from Norishige Kanai's Hometown of Chiba, Japan")
