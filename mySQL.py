# import mysql.connector

class MySQL:

    def __init__(self,username='', password='', host='', database=''):
        self.username = username
        self.password = password
        self.host = host
        self.database = database
        # self.cnx = mysql.connector.connect(user=self.username, password=self.password,host=self.host,database=self.database)
        # self.cursor = cnx.cursor()

    def query(self,querys,formats=''):
        return_list = []
        cursor.execute(querys,formats)
        for data in cursor:
            return_list.append(data)
        return return_list

    def close(self):
        cursor.close()
        cnx.close()
