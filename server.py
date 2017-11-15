from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
from urllib import parse
import threading

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_path = parse.urlparse(self.path)
        print(parsed_path)
        path= self.path
        realpath= parsed_path.path
        querys = parsed_path.query
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write("Hello world!!!".encode('utf-8'))       

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    pass


if __name__ == '__main__':
    host = 'localhost'
    port = 5000
    server = ThreadedHTTPServer((host, port), Handler)
    print('Starting server on %s port: %s, use <Ctrl-C> to stop' % (host, port))
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    server.server_close()
    print('server is closed.')