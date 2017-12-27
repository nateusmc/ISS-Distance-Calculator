# ISS Distance Calculator

Helpful Links:

http://iss.astroviewer.net/observation.php?lon=-96.51430870000002&lat=33.3349924&name=75409

http://open-notify.org/Open-Notify-API/ISS-Location-Now/

https://api.nasa.gov/index.html#getting-started

https://wheretheiss.at/w/developer

https://math.stackexchange.com/questions/1416288/how-to-calculate-distance-from-the-international-space-station-given-coordinates

https://stackoverflow.com/questions/10473852/convert-latitude-and-longitude-to-point-in-3d-space

https://www.dataquest.io/blog/python-api-tutorial/

##

## Notes on mathematical theory to calculate the distance

- Pythagorean Theorem
- Radius of earth is a constant
- Center of earth is origin
- Convert lat and long into absolute position
- Assume the earth does not spin

##

## Interesting Facts:
- ISS moves at a rate of 28,000 km/h

- The radius of the Earth is about 6,400km

- the ISS is about 400km above the surface

- It takes the ISS approximately 90 minutes to travel a full rotation around the Earth


##

## How to calculate:

The radius of the Earth is about 6,400km, the ISS is about 400km above the surface, so 
r1=6400,
r2=6800
Then substitute the longitudes & latitudes (in radians) to compute the 
(x,y,z) coordinates of the two points and then compute the
Euclidean distance between the two points.

##

## Current crew members on expedition 54:

### United States:

Joseph M. Acaba from Anaheim, California:
Latitude and Longitude: 33.836636, -117.914221
33°50'19.9"N 117°54'51.8"W
https://www.nasa.gov/astronauts/biographies/joseph-m-acaba/biography

Mark T. Vande Hei from Falls Church, Virginia:
Latitude and Longitude: 38.882412, -77.173007
38°52'56.7"N 77°10'22.8"W
https://www.nasa.gov/astronauts/biographies/mark-t-vande-hei/biography

Scott D. Tingle from Randolph, Massachusetts:
Latitude and Longitude: 42.180009, -71.054176
42°10'48.0"N 71°03'15.0"W
https://www.nasa.gov/astronauts/biographies/scott-d-tingle/biography

##

### Russia:

Alexander Alexandrovich from Orel (Oryol), Russia:
Latitude and Longitude: 52.967776, 36.059538
52°58'04.0"N 36°03'34.3"E
http://www.gctc.ru/main.php?id=192

Anton Nikolaevich from Sevastopol, Russia:
Latitude and Longitude: 53.456705, 35.185575
53°27'24.1"N 35°11'08.1"E
http://www.gctc.ru/main.php?id=218

##

### Japan:

Norishige Kanai from Chiba, Japan:
Latitude and Longitude: 35.620887, 140.107225
35°37'15.2"N 140°06'26.0"E
http://iss.jaxa.jp/en/astro/biographies/kanai/index.html

##
