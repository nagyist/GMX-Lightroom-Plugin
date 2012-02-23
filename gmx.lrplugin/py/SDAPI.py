#!/usr/bin/env python
from urllib import urlencode
from urllib2 import Request, urlopen, HTTPError, build_opener, install_opener, HTTPCookieProcessor
import json, cookielib

UAS_URL = 'https://uas2.uilogin.de/login'
UAS_SID = 'gmx.mobile.fotoservice.live'
USER_AGENT = 'Lightroom-Plugin/0.1'

class InvalidStateException(Exception):
    pass

class SDAPI(object):

    def __init__(self):
        self.session_id = None
        self.service_uri = None
        self.cookies = cookielib.LWPCookieJar()
        hto = build_opener(HTTPCookieProcessor(self.cookies))
        install_opener(hto)


    def login(self, user, password):
        data = urlencode({
            'serviceID': UAS_SID,
            'username':  user,
            'password':  password,
        })
        headers = {
            'User-Agent': USER_AGENT,
            'Accept': 'application/json',
        }
        req = Request(UAS_URL, data, headers)
        try:
            resp = urlopen(req)
            sctx = json.load(resp)
            self.service_uri = '%sprimaryEmail' % sctx['PhotoAlbum']['baseURI']
            self.session_id = resp.geturl().split(';')[1]
        except HTTPError, e:
            print e

    def assert_loggedin(self):
        if self.session_id is None:
            raise InvalidStateException('session_id')
        if self.service_uri is None:
            raise InvalidStateException('service_uri')

    def get_albums(self):
        self.assert_loggedin()
        return self.call_rest('Albums?onlyAlbums=true')['albums']

    def call_rest(self, uri):
        headers = {
            'User-Agent': USER_AGENT,
            'Accept': 'application/json',
        }
        req = Request('%s/%s' % (self.service_uri, uri), None, headers)
        try:
            resp = urlopen(req)
            return json.load(resp)
        except HTTPError, e:
            print e
            print e.read()



if __name__ == '__main__':
    import sys
    api = SDAPI()
    api.login(sys.argv[1], sys.argv[2])
    for album in api.get_albums():
        print album['name']
