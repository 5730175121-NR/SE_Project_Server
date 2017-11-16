from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
from urllib import parse
from url_management import url_management
from decimal import Decimal
import threading
import json

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_path = parse.urlparse(self.path)
        path= self.path
        realpath= parsed_path.path
        querys = parsed_path.query
        response = url_management(realpath, querys)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode('utf-8'))       

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    pass


if __name__ == '__main__':
    host = 'localhost'
    port = 5000
    try:
        configuration_file = open('configuration','r')
        configuration = {}    
        for line in configuration_file.readlines():
            line = line.strip('\n')
            (key,val) = line.split(':')
            configuration[key] = val
        if 'host' in configuration:
            host = configuration['host']
        if 'port' in configuration:
            port = int(configuration['port'])
        configuration_file.close()
    except:
        configuration_file = open('configuration','w')
        configuration_file.write("host:localhost\nport:5000")
        configuration_file.close()
        print('configuration file is not found : use "localhost" and port : 8080 as default')
        pass
    server = ThreadedHTTPServer((host, port), Handler)
    print('Starting server on %s port: %s, use <Ctrl-C> to stop' % (host, port))
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    server.server_close()
    print('server is closed.')