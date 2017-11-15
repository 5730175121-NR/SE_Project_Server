from mySQL import MySQL
from caller import Caller

def path_spliter(path):
    return path.split('/')

def query_spliter(querys):
    if querys == '':
        return {}
    querys_dict = {}
    querys_list = querys.split('&')
    for query in querys_list:
        temp = query.split('=')
        querys_dict[temp[0]] = temp[1]
    return querys_dict

def url_management(path, querys):
    path_list = path_spliter(path)
    print(path_list)
    querys_dict = query_spliter(querys)
    if path_list[1] == 'caller':
        return caller(path_list, querys_dict)

def caller(path_list, querys_dict):
    caller = Caller()
    if path_list[2] == 'searchtaxi':
        return caller.searchTaxi()
    