from PIL import Image 
from HackThisSite import *
import urllib2
import os


translater = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' 
        }



#Log in and open html page for reading 
username = "XXXXXXXX"
password = "XXXXXXXX"
hts = HackThisSite(username, password)
url = "https://www.hackthissite.org/missions/prog/2/index.php"
html_page = hts.login_and_read_page_we_want(url)



#download wordlist.txt
download_link = "https://www.hackthissite.org/missions/prog/2/PNG"
open_link = urllib2.urlopen(download_link)

with open("PNG.png", 'w') as wordlist:
    wordlist.write(open_link.read())

#Open Image and find data
hts_image = Image.open("PNG.png")
pix = hts_image.getdata() #where 0 is black and 1 is white pixel



temp = 0
current_pix = 0
main_list = []
for pixel in list(pix):
    current_pix += 1
    if pixel == 1:
        main_list.append(current_pix - temp)
        temp = current_pix

main_list[0] = main_list[0] - 1 #this is to make sure that we fix the offset we created with the first pixel by starting the count at 1
main_list = [chr(i) for i in main_list]
morse_code_string = "".join(main_list)
morse_code_string = morse_code_string.replace("/", "")
print morse_code_string

morse_code_list = morse_code_string.split(" ")
morse_code_list = filter(None, morse_code_list)


eng_list = []
for code in morse_code_list:
    for k, v in translater.items():
        if code in v and len(code) == len(v):
            eng_list.append(k)

answer = "".join(eng_list)
print answer

hts.send_answer(answer, url)
print hts.send_answer(answer, url)
os.remove("PNG.png")
