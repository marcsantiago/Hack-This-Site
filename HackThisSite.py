#!/usr/bin/env python2.7
import urllib
import urllib2
import cookielib


class HackThisSite:
    
    # create constructor that takes user name and password and pass tht data to the login methods
    my_username = ""
    my_password = ""

    def __init__(self, username, password):
        self.my_username = username
        self.my_password = password

    values = {'Host': 'www.hackthissite.org',
              'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0)',
              'Referer':'http://www.hackthissite.org/user/login',
              'Content-Type':'application/x-www-form-urlencoded',
              'Accept-Encoding':'gzip,deflate',
              }   
    
    # This allows us to login as well as read the page we want
    def login_and_read_page_we_want(self, link__to_page_we_want_to_open):
        """Just pass it the url to the page where the hts problem is"""
        self.host = 'www.hackthissite.org'
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 6.0)'
        self.referer = 'http://www.hackthissite.org/user/login'
        self.content_type = 'application/x-www-form-urlencoded'
        self.accept_encoding = 'gzip,deflate'
        self.body = {'username': self.my_username, 'password': self.my_password}

        #build cookie handler
        self.cj = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
        self.opener.addheaders.append(('Referer',link__to_page_we_want_to_open))
        urllib2.install_opener(self.opener)
        
        #encode request information
        self.data = urllib.urlencode(self.body)
        
        #send login information
        self.req = urllib2.Request(self.referer, self.data, self.values)
        self.page = urllib2.urlopen(self.req)
        
        #return the html page we are are going to work with
        self.url = link__to_page_we_want_to_open
        self.page = urllib2.urlopen(self.url)
        
        return self.page.read()
    
    # this allows for the spitting of a string with any number of delimiters
    def tsplit(self, s, sep):
        stack = [s]
        for char in sep:
            pieces = []
            for substr in stack:
                pieces.extend(substr.split(char))
                stack = pieces
        return stack

    # Submit hts form data
    def send_answer(self, data_to_send, page_to_send_data_to):
        #for mission 12 you will need to change the code to
        #form_data = {'solution' : data_to_send, "submitbutton" : "Submit"}
        self.form_data = {'solution' : data_to_send}
        self.encoded_data = urllib.urlencode(self.form_data)
        self.referer = page_to_send_data_to
        self.req = urllib2.Request(self.referer, self.encoded_data, self.values)
        self.page = urllib2.urlopen(self.req)
        return self.page    
