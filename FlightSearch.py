import json
import urllib2

class FlightSearch(object):
  
  def __init__(self, goingFrom, goingTo, roundTrip=false):
	json_data = urllib2.urlopen('http://www.flightradar24.com/zones/full_all.json')
	self.data = json.load(json_data)
	json_data.close() 
    self.goingFrom=goingFrom
    self.goingTo=goingTo
    self.roundTrip=roundTrip
    # Parse this stuff later from the JSON file. 
    price = 
    return price

	# in case this is a private class we need getters/setters    
  def getDates(self, departureDate, returnDate = null):
  	# Do fancy JSON stuff here

  def disp_goingfrom(self):
  	return self.goingfrom

  def disp_goingto(self):
  	return self.goingTo

# Means that if you run this script directly from file instead of importing... do this:
if __name__ == '__main__':
	startPlace = raw_input("Departing City? (ex:\'LA\'')")
	endPlace = raw_input("Returning City? (ex:\'LA\')")
	departureDate = raw_input("When are you leaving? (MM/DD/YYYY)")
	roundTrip = raw_input("Is it roundtrip(Y/N)?")
	if roundtrip == 'Y':
		returnDate=raw_input("When are you returning (MM/DD/YYYY)")
	else:
		returnDate = null
	print('\nLoading your data...\n')
	try:
		myflight=FlightSearch(startPlace, endPlace)
	except ValueError:
		print ('! Incorrect Input !')
	print myflight.getDates(departureDate)
