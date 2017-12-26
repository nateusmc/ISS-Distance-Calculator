#ISS Distance Calculator

Helpful Links:

http://iss.astroviewer.net/observation.php?lon=-96.51430870000002&lat=33.3349924&name=75409

http://open-notify.org/Open-Notify-API/ISS-Location-Now/

https://api.nasa.gov/index.html#getting-started

https://wheretheiss.at/w/developer

##

#Notes on mathematical theory to calculate the distance

pythagorean theorem

Radius of earth is a constant

Center of earth is origin

ISS rotates 400km outside of earth’s equator

Pathagorous theorem
Convert lat and long into absolute position
Assume the earth does not spin

#How to calculate:

The radius of the Earth is about 6,400km, the ISS is about 400km above the surface, so 
r1=6400,
r2=6800
Then substitute the longitudes & latitudes (in radians) to compute the 
(x,y,z) coordinates of the two points and then compute the
Euclidean distance between the two points.
