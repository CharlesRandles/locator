#!/usr/bin/python

import cgi

import cgitb
cgitb.enable()

MAX_INPUT_LENGTH=0x100 #Quite long enough thank you so very much.

LOCATION_FILENAME="chaz_location.txt"

def get_val(data, key):
    if key in data:
        return data[key].value
    else:
        return "0.0"

class SanityException(Exception):
    pass

def sanity_check(val):
    """We're looking for a decimal representaion
    of a lat, long or alt. so, +-. digits are all we'll accept.
    Also, no silly buggers with long strings.
    Could do this with a regex. But then I'd have two problems."""

    if len(val) > MAX_INPUT_LENGTH:
        raise SanityException("%d is a stupid length for an input" % len(val))

    valid_chars="+-.1234567890"
    for c in val:
        if c not in valid_chars:
            raise SanityException("%s is not a valid character for a lat/long/alt" % c)

    #No evidence for insanity found
    return True
        
def refuse(reason):
    print """Content-Type: text/html

    <head><title>Nope.</title></head>
    <body>
    Nope. This is why:
    <br />
    %s
    </body>
    """ % reason

def store_and_return(lat, long, alt):

    #Store the data, one datum per line, overwriting the previous data
    location_file=open(LOCATION_FILENAME, "w")
    location_file.write("%s\n%s\n%s\n" % (lat, long, alt))
    location_file.close()

    #return 200, and a form for updating the data.
    print """Content-Type: text/html

    <head><title>Where's Chaz?</title></head>
    <body>
    lat=%s
    <br />
    long=%s
    <br />
    alt=%s
    <div class="reload-form">
        <form method="POST" target="update_location.py">
        <table>
        <tr> <td>Latitude:</td> <td><input type="text" name="latitude" /></td> </tr>
        <tr> <td>Longitude:</td> <td><input type="text" name="longitude" /></td> </tr>
        <tr> <td>Altitude:</td> <td><input type="text" name="altitude" /></td> </tr>
        <tr><td><input type="submit"></td></tr>
        </table>
        </form>
    </div>
    </body>
""" % (lat, long, alt)

#Grab the location data
data=cgi.FieldStorage()
lat=get_val(data, "latitude")
long=get_val(data, "longitude")
alt=get_val(data, "altitude")

#Do a basic sanity check on the data, proceed only if we think it's safe
try:
    map(sanity_check, [lat, long, alt])
    store_and_return(lat, long, alt)
except SanityException as insanity:
    refuse(insanity)
