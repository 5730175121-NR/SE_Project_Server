import datetime 

class Position:

    def __init__(self, latitude=0.0, longitude =0.0, timestamp= ''):
        self.latitude = latitude
        self.longitude = longitude
        self.timestamp = timestamp

    def isValid(self):
        return True
    
    def getUserPosition(self, name):
        return ['null']

    def getLocationName(self, latitude, longitude):
        return 'no place'

    def setLocation(self, latitude, longitude):
        self.timestamp = datetime.datetime.now()
        self.latitude = latitude
        self.longitude = longitude
    
