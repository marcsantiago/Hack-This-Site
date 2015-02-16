from HackThisSite import *
import math

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    sqr = int(math.sqrt(n)) + 1
    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

def comp_prime_product(number_list):
    prime_numbers = []
    composite_numbers =[]
    for num in number_list:
        if is_prime(int(num)):
            prime_numbers.append(int(num))
        else:
            composite_numbers.append(int(num))
            
    composite_numbers = [i for i in composite_numbers if i != 1]
    composite_numbers = [i for i in composite_numbers if i != 0]

    return sum(prime_numbers) * sum(composite_numbers)

def trunc_and_shift(char_list):
    char_list = char_list[:25]
    result = ""
    for char in char_list:
        x = ord(char)
        result += chr(x + 1)

    return result


def generate_answer_from_raw_string(string):
    '''Returns the answer to the problem'''
    numbers = []
    letter = []
    for ch in string:
        if ch.isdigit():
            numbers.append(ch)
        else:
            letter.append(ch)
    return trunc_and_shift(letter) + str(comp_prime_product(numbers))
        
        
    


# create local variables to hold user name, password, and url of the page we are working with
username = "XXXXXXXXXXXXXXX"
password = "XXXXXXXXXXXXXXX"

#create an instance of the class
# pass login information to HackThisSite constructor
hts = HackThisSite(username, password)


#login hackthisiste and store the html code of programming mission 12
url = "https://www.hackthissite.org/missions/prog/12/index.php"
page_contents = hts.login_and_read_page_we_want(url)

#find the start and end of string we want
start_of_string = str(page_contents).find("String:")
end_of_string = str(page_contents).find("<form")
data_string = page_contents[start_of_string+38:end_of_string-17]


# call generate_answer_from_raw_string to return the answer
data = generate_answer_from_raw_string(data_string)

# send data
hts.send_answer(data, url) #see the HackThisSite.py file for special note about sending data on this mission
