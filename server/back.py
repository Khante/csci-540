import os,urlparse,requests,cgi,json

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
            res = queryHandle(qprsd)
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
        self._set_headers()
        ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
        if ctype == 'multipart/form-data':
            postvars = cgi.parse_multipart(self.rfile, pdict)
        elif ctype == 'application/x-www-form-urlencoded':
            length = int(self.headers.getheader('content-length'))
            postvars = cgi.parse_qs(self.rfile.read(length), keep_blank_values=1)
        else:
            postvars = {}

        s=postvars['service'][0]
        if s == 'newsPost':
            channel = postvars['channel'][0]
            url ='http://news:5000/publish/'
            name = 'John Hancock'
            
            news = postvars['text'][0]
            requests.post(url, json={'name':name,'channel':channel,'news':news})
        # self.wfile.write()




#Return a string/html of the query results
#args has whatever the client sent as a dictionary.
def queryHandle(args):
    s=args['service'][0]
    if s == 'review':
        print 'Review service selected'
        url='http://reviews:8080/api/reviews/%s'%args['title'][0]
        r = requests.get(url).json()
        s=''
        for c in r:
            s+='Score:%s Text:%s <br/>'%(c['review_score'] , c['review_text'])
        return s

    elif s == 'info':
        print 'Info service selected'
        url='http://info:5000/games/%s'%args['title'][0]
        r = requests.get(url)
        res = r.json()
        s = ''
        for r in res:
            if 'description' in r:
                s+=r['description']+'<br/>'
        return s
    elif s == 'sub': #
        print 'News service selected'
        channel=args['title'][0]
        url='http://news:5000/subscribe/'
        r = requests.post(url, json={'name':'DK. DonkeyKong','channel': channel}, headers={'Content-type': 'application/json'})
        return ''
    elif s == 'poll':
        url='http://news:5000/publications/%s'%args['title'][0]
        r=requests.get(url)
        res = r.json()
        return str(res)
        # get a big string of all subscribed news
    elif s == 'listsub':
        url='http://news:5000/subscriptions/'
        r = requests.get(url)
        return r.json()
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