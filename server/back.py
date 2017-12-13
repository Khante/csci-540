import os,urlparse,requests,cgi

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
            res = cgi.escape(str(queryHandle(qprsd)))
            print 'Res:',res
            self.wfile.write(res)
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
    s=args['service'][0]
    if s == 'review':
        print 'Review service selected'
        url='http://reviews:8080/api/reviews/%s'%args['title'][0]
        r = requests.get(url)
        print r
        return r.text

    elif s == 'info':
        print 'Info service selected'
        url='http://news:5000/%s'%args['title'][0]
        r = requests.get(url)
        return r.text

    elif s == 'news':
        print 'News service selected'
        channel=args['title'][0]
        url='http://news:5001/subscribe/'
        data={'channel': channel}
        r = requests.post(url, data=data)
        print r
        return r.text
    elif s == 'poll':
        pass
        # get a big string of all subscribed news
    else:
        print s
    return 'Not implemented'


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