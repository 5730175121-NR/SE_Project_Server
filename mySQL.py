import pymysql

class MySQL:

    def __init__(self,username='', password='', host='', port='', database=''):
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        self.cnx = pymysql.connect(host=self.host, port=self.port, user=self.username, passwd=self.password, db=self.database)
        self.cursor = self.cnx.cursor()

    def query(self,querys,formats=''):
        return_list = []
        if formats == '':
            self.cursor.execute(querys)
        else:
            self.cursor.execute(querys,formats)
        for data in self.cursor:
            return_list.append(data)
        return return_list

    def close(self):
        self.cursor.close()
        self.cnx.close()
