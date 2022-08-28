Geosphere
=========

This small pure python package provides two functions which do
computations in spherical trigonometry that are needed for
navigating on the surface of the earth.

The function

``destination(lat_deg, long_deg, distance_nm, bearing_deg)``

returns the latitude and longitude of the location
reached by traveling distance_nm nautical miles along the great circle
route starting at the location with latitude lat_deg and longitude
long_deg and having the specified initial bearing.

The function

``distance_bearing(lat1_deg, long1_deg, lat2_deg, long2_deg)``

returns the distance in nautical miles and the bearing in degrees from
the location given by the first latitude-longitude pair to the
location given by the second latitude-longitude pair.  If the points
are too close together the bearing is 0.  If the first point is at a
pole, the bearing is 0 or 180, as appropriate.  If the points are
antipodes, so the bearing is undefined, then the bearing returned
is 0.


