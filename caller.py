from user import User
from mySQL import MySQL

class Caller(User):

    def callTaxi(self):
        print('call taxi!!')

    def searchTaxi(self):
        mysql = MySQL()
        min_latitude = self.user_position.latitude - 5.0
        max_latitude = self.user_position.latitude + 5.0
        min_longitude = self.user_position.longitude - 5.0
        max_longitude = self.user_position.longitude + 5.0
        list_of_results = mysql.query('SELECT * FROM gettaxi.driver WHERE ((real_time_lat_location BETWEEN %s AND %s) AND (real_time_long_location BETWEEN %s AND %s))', (min_latitude,max_latitude,min_longitude,max_longitude))
        list_of_taxi = []
        for result in list_of_results:
            (phone, isActive, status, real_time_lat, real_time_long, license_no, ssn, driver_premission_id) = result
            real_time_lat = float("{0:.6f}".format(real_time_lat))
            real_time_long = float("{0:.6f}".format(real_time_long))
            list_of_taxi.append((phone, isActive, status, real_time_lat, real_time_long, license_no, ssn, driver_premission_id))
        mysql.close()
        return list_of_taxi

    def bookTaxi(self):
        print('booking')

    def paid(self, transactionID):
        print('paid')