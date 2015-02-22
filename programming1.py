#!/usr/bin/env python2.7
class FileParser:
    
    word_list = ""
    sword_list = ""
    cleaned_word_list = []
    cleaned_scrambled_word_list = []
    wordlist_dictionary = {}

    def __init__(self, wlist, scrambled_word_list):
        self.word_list = wlist
        self.sword_list = scrambled_word_list

    def read_and_clean_files(self):
        
        with open(self.word_list, 'r') as clean_word_list:  #opens and cleans the wordlist provided by HackThisSite.org
            clean_word_list = list(clean_word_list)
            clean_word_list = [str(word).strip() for word in clean_word_list]
            self.cleaned_word_list = clean_word_list
        
        with open(self.sword_list, 'r') as clean_scrambled_word_list:  #File you save the scrammbled words to
            clean_scrambled_word_list = list(clean_scrambled_word_list)
            clean_scrambled_word_list = [str(word).strip() for word in clean_scrambled_word_list]
            self.cleaned_scrambled_word_list = clean_scrambled_word_list
        
        return self.cleaned_word_list, self.cleaned_scrambled_word_list

    def create_word_list_dictionary(self, cleaned_word_list):
        sorte_test_words = []
        for word in xrange(len(self.cleaned_word_list)):
            temp_string = ""
            sorted_words = sorted(str(cleaned_word_list[word]))
            for ch in sorted_words:
                temp_string += ch
            sorte_test_words.append(temp_string)
        
        return dict(zip(cleaned_word_list, sorte_test_words))

    def sort_scram_words(self, cleaned_scrambled_word_list):
        sorted_test_words = []
        for word in xrange(len(self.cleaned_scrambled_word_list)):
            temp_string = ""
            sorted_words = sorted(str(cleaned_scrambled_word_list[word]))
            for ch in sorted_words:
                temp_string += ch
            sorted_test_words.append(temp_string)
    
        return sorted_test_words
    

def main():
    
    import sys
    import os
    
    word_list_file = sys.argv[1]
    scrambled_word_list_file = sys.argv[1]

    if not os.path.isfile(word_list_file):
        print("Usage: python programming.py [wordlist.txt] [scrammbled_word_list.txt]\n\
        The word list file you have entered was not found.\n"
              "Check spelling and or make sure the file is in the same directory as the script")
        sys.exit(1)
    
    if not os.path.isfile(scrambled_word_list_file):
        print("Usage: python programming.py [wordlist.txt] [scrammbled_word_list.txt]\n\
        The scrammbled word list file you have entered was not found.]\n"
              "Check spelling and or make sure the file is in the same directory as the script")
        sys.exit(1)    
    
    fl = FileParser(word_list_file, scrambled_word_list_file)
    wordlist, scrambledwordlist = fl.read_and_clean_files()
    mydict = fl.create_word_list_dictionary(wordlist)
    scrambledwords = fl.sort_scram_words(scrambledwordlist)
    
    string = ""
    for m in scrambledwords:
        for k, v in mydict.items():
            if m in v and len(m) == len(v):
                string += k + ","
    print string[:-1]

    
main()
