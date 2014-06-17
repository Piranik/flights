#!/usr/local/bin/python2.7
class FlightSearch(object):
  def __init__(self, goingFrom, goingTo, roundTrip):
    self.goingFrom=goingFrom
    self.goingTo=goingTo
    self.roundTrip=roundTrip
    print roundTrip
  def getDates(self):
    if self.roundTrip==0:
      #It's oneway
      departureDate = raw_input("When are you leaving? ( MM/DD/YYYY")
    else:
      #It's roundtrip
      departureDate = raw_input("When are you leaving? ( MM/DD/YYYY) ")
      returnDate=raw_input("When are you returning ( MM/DD/YYYY) ")
print 'hi'
flight=FlightSearch('PHL', 'ATL', 0)
print 'hey'
flight.getDates()
