import requests

info = requests.get('http://api.open-notify.org/iss-now.json').json()
print('The ISS\'s Position is: ',
      info['iss_position']['latitude'],
      info['iss_position']['longitude'])

myPosInfo = requests.get('http://ip-api.com/json').json()
print('Your location is: ', myPosInfo['lat'], myPosInfo['lon'])
