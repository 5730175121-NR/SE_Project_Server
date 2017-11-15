from user import User
from mySQL import MySQL

class Caller(User):

    def callTaxi(self):
        print('call taxi!!')

    def searchTaxi(self):
        mysql = MySQL()
        list_of_taxi = mysql.query('SELECT * FROM gettaxi.driver')
        mysql.close()
        print('return Object')
        return list_of_taxi

    def bookTaxi(self):
        print('booking')

    def paid(self, transactionID):
        print('paid')