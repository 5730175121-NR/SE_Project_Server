from user import User
from mySQL import MySQL

class Caller(User):

    def callTaxi(self):
        print('call taxi!!')

    def searchTaxi(self):
        mysql = MySQL()
        list_of_results = mysql.query('SELECT * FROM gettaxi.driver')
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