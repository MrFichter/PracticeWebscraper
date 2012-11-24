import urllib2 ## There's also urllib.
response = urllib2.urlopen ('http://api.wunderground.com/api/063bc5d3a98d95bf/conditions/q/DC/Washington.json')
## Note the very end of the URL. It's a query about weather in DC.
## I created a weather underground account and got a key. Did I need it to do the above?
import json
forecast = json.load (response)
## Response is the parent in a big, nested dictionary that weather underground displays.
## forecast ['current observation'] would return all of the data nested under 'current observation' on the web page.
print forecast ['current_observation']['temp_f'] #This returns just one item from the web page: the temp in Fahrenheit.
