#!/usr/bin/python

import cgi

import cgitb
cgitb.enable()

LOCATION_FILENAME="chaz_location.txt"
    
#OK, now write a map

def http_headers():
    return """Content-Type: text/html

    """

def google_map(lat, long):
    """ Write html/js code for creating a google map """
    return """
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no" />
    <style type="text/css">
      html { height: 100% }
      body { height: 100%; margin: 0; padding: 0 }
      #map-canvas { height: 100% }
    </style>
    <script type="text/javascript"
      src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBjgdfoiHLvChKKGfqOQHryhFyWapPPzy0&sensor=false">
    </script>
   <script type="text/javascript">
      function initialize() {
        var latLng = new google.maps.LatLng(""" + lat + "," + long + """);
        var mapOptions = {
          center: latLng,
          zoom: 15,
          mapTypeId: google.maps.MapTypeId.ROADMAP
        };
        var map = new google.maps.Map(document.getElementById("map-canvas"),
            mapOptions);
        var marker = new google.maps.Marker({
            position: latLng,
            map: map,
            title: 'Chaz!'
            });
      }
      google.maps.event.addDomListener(window, 'load', initialize);
    </script>
    """

def html_header():
    return """
    <head>
    <title>Where's Chaz?</title>
    %s
    </head>
    """ % google_map(lat, long)

def html_pos_text(lat, long, alt, time):
    return """
    <div class="table">
    <table>
    <tr><td>Lat:</td><td>%s</td></tr>
    <tr><td>Long:</td><td>%s</td></tr>
    <tr><td>Alt:</td><td>%s</td></tr>
    <tr><td>Time:</td><td>%s</td></tr>
    </table>
    </div>
    """ % (lat, long, alt, time)

def map_div():
    return """
        <div id="map-canvas" />
        
    """

def write_page(lat, long, alt):
    print http_headers()
    print "<html>"
    print html_header()
    print"<body>"
    print html_pos_text(lat, long, alt, time)
    print map_div()
    print"</body>"
    print "</html>"

#Read the location
try:
    (lat, long, alt, time) = open(LOCATION_FILENAME).readlines()
except ValueError as e:
    (lat, long, alt, time) = ("0.0", "0.0", "0.0", "Unknown")

lat=lat.strip()
long=long.strip()
alt=alt.strip()
time=time.strip()

write_page(lat, long, alt)

