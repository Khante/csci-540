import os
import urlparse
#!/usr/bin/env python
"""
Send a GET request::
    curl http://localhost
Send a HEAD request::
    curl -I http://localhost
Send a POST request::
    curl -d "foo=bar&bin=baz" http://localhost
"""
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        prsd= urlparse.urlparse(self.path)
        if prsd.query != '':
            qprsd = urlparse.parse_qs(prsd.query)
            print qprsd
            self.wfile.write(queryHandle(qprsd))
        else:
            self.path='.'+self.path
            if os.path.isdir(self.path):
                self.path+='/index.html'
            f=open(self.path)
            self.wfile.write(f.read())

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        pass


#Return a string/html of the query results
#args has whatever the client sent as a dictionary.
def queryHandle(args):
    pass
        
def run(server_class=HTTPServer, handler_class=S, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()