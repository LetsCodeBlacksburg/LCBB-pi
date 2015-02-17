#!/usr/bin/env python 
import pywapi
import string
import poplib

# Automatically geolocate the connecting IP
weather_com_result = pywapi.get_weather_from_weather_com(24060)
print "Weather.com says: It is " + string.lower(weather_com_result['current_conditions']['text']) + " and " + weather_com_result['current_conditions']['temperature'] + "C here.\n\n"

m = poplib.POP3_SSL('pop.googlemail.com', '995') 
m.user("username")
m.pass_("password")
count = m.stat()
print(count)