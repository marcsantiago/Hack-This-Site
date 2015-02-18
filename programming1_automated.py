from HackThisSite import *
import urllib2
import zipfile
import os


def sort_scram_words(cleaned_scrambled_word_list):
    sorted_test_words = []
    for words in xrange(len(cleaned_scrambled_word_list)):
        temp_string = ""
        sorted_words = sorted(str(cleaned_scrambled_word_list[words]))
        for ch in sorted_words:
            temp_string += ch
        sorted_test_words.append(temp_string)

    return sorted_test_words


def wordlist_dictionary_creator(cleaned_word_list):
    sorted_test_words = []
    for words in xrange(len(cleaned_word_list)):
        temp_string = ""
        sorted_words = sorted(str(cleaned_word_list[words]))
        for ch in sorted_words:
            temp_string += ch
        sorted_test_words.append(temp_string)

    return dict(zip(cleaned_word_list, sorted_test_words))


def read_wordlist(word_list):
    with open(word_list, 'r') as clean_word_list:  # opens and cleans the wordlist provided by HackThisSite.org
        clean_word_list = list(clean_word_list)
        clean_word_list = [str(word).strip() for word in clean_word_list]
    return wordlist_dictionary_creator(clean_word_list)  #pass wordlist to wordlist_dictionary_creator()/
                                                         #and return the dictionary


#Log in and open html page for reading 
hts = HackThisSite("XXXXXXXXXX", "XXXXXXXXX")
url = "https://www.hackthissite.org/missions/prog/1/index.php"
html_page = hts.login_and_read_page_we_want(url)

#####################Extracting wordlist.zip From Site#########################

#download wordlist.txt
download_link = "https://www.hackthissite.org/missions/prog/1/wordlist.zip"
open_link = urllib2.urlopen(download_link)

with open("wordlist.zip", 'w') as wordlist:
    wordlist.write(open_link.read())

#unzip downloaded wordlist
zfile = zipfile.ZipFile('wordlist.zip')
zfile.extractall()

#delete unneed zipfile
os.remove("wordlist.zip")

#create a dictionary where the keys are the words from the wordlist
#and the value is the same word sorted alphanumerically
wordlist_dictionary = read_wordlist("wordlist.txt")

##############Extracting Scrambled Words From html_page Variable###############

start_of_list = str(html_page).find("List of scrambled words:")  #finds a starting place of the scrambled list
end_of_list = str(html_page).find('name="submitform"')  #finds the ending place
dirty_list = str(html_page)[start_of_list + 42:end_of_list - 282]   #by adding 42 places and subtracting
                                                                    # 282 places the html content is clearer
items_to_replace = ["<td>", "</td>", "<li>", "</li>", "<tr>", "</tr>", " "]  #makes a list of things that we want removed
cleaned_scrambled_list = hts.tsplit(dirty_list, items_to_replace)
cleaned_scrambled_list = [i for i in cleaned_scrambled_list if i != "\n"]  #remove extra newlines in list
cleaned_scrambled_list = filter(None, cleaned_scrambled_list)  #makes sure there are no empty items in list,
                                                               #we a list length of ten

sorted_scrambled_list = sort_scram_words(cleaned_scrambled_list)
 

string = ""
for word in sorted_scrambled_list:
    for k, v in wordlist_dictionary.items():
        if word in v and len(word) == len(v):
            string += k + ","
data = string[:-1]

#send data to hts
os.remove("wordlist.txt")
hts.send_answer(data, url)
print hts.send_answer(data, url)
