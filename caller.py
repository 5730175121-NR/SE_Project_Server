from user import User

class Caller(User):

    def callTaxi(self):
        print('call taxi!!')

    def searchTaxi(self):
        print('return Object')

    def bookTaxi(self):
        print('booking')

    def paid(self, transactionID):
        print('paid')