class fileParser:
    
    word_list = ""
    sword_list = ""
    cleaned_word_list = []
    cleaned_scrammbled_word_list = []
    wordlist_dictionary = {}


    def __init__(self, wlist, scrammbled_word_list):
        self.word_list = wlist
        self.sword_list = scrammbled_word_list
    
   
    def read_and_clean_files(self):
        
        with open(self.word_list, 'r') as clean_word_list: # opens and cleans the wordlist provided by HackThisSite.org
            clean_word_list = list(clean_word_list)
            clean_word_list = [str(word).strip() for word in clean_word_list]
            self.cleaned_word_list = clean_word_list
        
        with open(self.sword_list, 'r') as clean_scrammbled_word_list: # File you save the scrammbled words to
            clean_scrammbled_word_list = list(clean_scrammbled_word_list)
            clean_scrammbled_word_list = [str(word).strip() for word in clean_scrammbled_word_list]
            self.cleaned_scrammbled_word_list = clean_scrammbled_word_list
        
        return self.cleaned_word_list, self.cleaned_scrammbled_word_list
    
        
    def create_word_list_dictionary(self, cleaned_word_list):
        sortedTestWords = []
        for word in xrange(len(self.cleaned_word_list)):
            tempString = ""
            sortedWords = sorted(str(cleaned_word_list[word]))
            for ch in sortedWords:
                tempString += ch
            sortedTestWords.append(tempString)
        
        return dict(zip(cleaned_word_list, sortedTestWords))
    
    
    def sort_scram_words(self, cleaned_scrammbled_word_list):
        sortedTestWords = []
        for word in xrange(len(self.cleaned_scrammbled_word_list)):
            tempString = ""
            sortedWords = sorted(str(cleaned_scrammbled_word_list[word]))
            for ch in sortedWords:
                tempString += ch
            sortedTestWords.append(tempString)
    
        return sortedTestWords
    

def main():
    
    import sys
    import os
    
    word_list_file = sys.argv[1]
    scrammbled_word_list_file = sys.argv[1]
    
    
    if not os.path.isfile(word_list_file):
        print("Usage: python programming.py [wordlist.txt] [scrammbled_word_list.txt]\nThe word list file you have entered was not found.\n"
              "Check spelling and or make sure the file is in the same directory as the script")
        sys.exit(1)
    
    if not os.path.isfile(scrammbled_word_list_file):
        print("Usage: python programming.py [wordlist.txt] [scrammbled_word_list.txt]\nThe scrammbled word list file you have entered was not found.]\n"
              "Check spelling and or make sure the file is in the same directory as the script")
        sys.exit(1)    
    
    fl = fileParser(word_list_file, scrammbled_word_list_file)
    wordlist, scrammbledwordlist = fl.read_and_clean_files()
    mydict = fl.create_word_list_dictionary(wordlist)
    scrammbledwords = fl.sort_scram_words(scrammbledwordlist)
    
    string = ""
    for m in scrammbledwords:
        for k , v in mydict.items():
            if m in v and len(m) == len(v):
                string += k + ","
    print string[:-1]

    
main()
