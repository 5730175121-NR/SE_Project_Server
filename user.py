from position import Position

class User:
  
    def __init__(self, facebookID= '', phoneNumber= '', password = '', dataOfBirth= '', firstName = '', lastName= '', address= ''):
        self.facebookID = facebookID
        self.phoneNumber = phoneNumber
        self.password = password
        self.dataOfBirth = dataOfBirth
        self.firstName = firstName
        self.lastName = lastName
        self.address = address
        self.user_position = Position()

    def login(self, phoneNumber, password):
        return -1

    def logout(self):
        return -1
    
    def editProfile(self, user):
        self.facebookID = user.facebookID
        self.phoneNumber = user.phoneNumber
        self.password = user.password
        self.dataOfBirth = user.dataOfBirth
        self.firstName = user.firstName
        self.lastName = user.lastName
        self.address = user.address
        return -1

    def sendRegEmail(self, email, password):
        return -1
