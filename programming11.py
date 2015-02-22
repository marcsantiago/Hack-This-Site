#!/usr/bin/env python2.7
import urllib
import urllib2
import cookielib

values = {'Host': 'www.hackthissite.org',
          'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0)',
          'Referer':'http://www.hackthissite.org/user/login',
          'Content-Type':'application/x-www-form-urlencoded',
          'Accept-Encoding':'gzip,deflate',
          }


def login(username, password):
    host = 'www.hackthissite.org'
    user_agent = 'Mozilla/4.0 (compatible; MSIE 6.0)'
    referer = 'http://www.hackthissite.org/user/login'
    content_type = 'application/x-www-form-urlencoded'
    accept_encoding = 'gzip,deflate'
    
    body = {'username': username, 'password': password}
    
    
    #build cookie handler
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    opener.addheaders.append(('Referer','https://www.hackthissite.org/missions/prog/11/index.php'))
    urllib2.install_opener(opener)
    
    #encode request information
    data = urllib.urlencode(body)
    
    #send login information
    req = urllib2.Request(referer, data, values)
    page = urllib2.urlopen(req)
    
    url = "http://www.hackthissite.org/missions/prog/11/"
    page = urllib2.urlopen(url)   
    
    return str(page.read())


def find_key(page):
    html_content = page
    key = html_content.find("Shift:")
    html_content_key = html_content[key+6:key+9]

    return int(str(html_content_key).replace('>',"").replace(" ","").replace('<', ""))


def tsplit(s, sep):
    stack = [s]
    for char in sep:
        pieces = []
        for substr in stack:
            pieces.extend(substr.split(char))
        stack = pieces
    return stack


def find_encrypted_string(page):
    html_content = page
    start_of_string = html_content.find("String:")
    end_of_string = html_content.find("Shift:")
    encrypted_string = html_content[start_of_string+8:end_of_string-12]
    encrypted_string = tsplit(encrypted_string, "!@#$%^&*()_+-={}[]\|;'\":<>?,./")
    encrypted_string = filter(None, encrypted_string)
    return encrypted_string


def get_cyphered_text(input_word, shift):
    shifted_input_wordlist = [chr(int(x) - int(shift)) for x in input_word]
    return ''.join(shifted_input_wordlist)


def send_answer(data_to_send):
    form_data = form_data = {'solution': data_to_send}
    encoded_data = urllib.urlencode(form_data)
    referer = "https://www.hackthissite.org/missions/prog/11/index.php"
    req = urllib2.Request(referer, encoded_data, values)
    page = urllib2.urlopen(req)
    return page


html_page = login("XXXXXXXXX", "XXXXXXXXX")
key = find_key(html_page)
encrytped_string = find_encrypted_string(html_page)
data = get_cyphered_text(encrytped_string, key)
send_answer(data)
print send_answer(data)
"""You can check your profile now to see that programming mission 11 was completed!"""
