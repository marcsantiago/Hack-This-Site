from random import choice
import pyminizip
import os
import zipfile

class OneTimePadEncryption:
    """This Class was designed to apply a one time pad encryption
    on textual data that either comes from a file or that is entered
    manually by the user. NOTE** the program can only handle the
    standard english alphabet, with  spaces, other punctuation
    has not been added yet"""
    def __init__(self):
        self.my_key = None
        self.my_string = None
        self.string_list = None
        self.key_list = None
        self.file_data = None

    alpha_dictionary = {
        0: ["a"],
        1: ["b"],
        2: ["c"],
        3: ["d"],
        4: ["e"],
        5: ["f"],
        6: ["g"],
        7: ["h"],
        8: ["i"],
        9: ["j"],
        10: ["k"],
        11: ["l"],
        12: ["m"],
        13: ["n"],
        14: ["o"],
        15: ["p"],
        16: ["q"],
        17: ["r"],
        18: ["s"],
        19: ["t"],
        20: ["u"],
        21: ["v"],
        22: ["w"],
        23: ["x"],
        24: ["y"],
        25: ["z"],
        26: [" "],
    }

    def string_converter(self, e_d_string_or_key_string):
        """Takes a given string whether it is the encrypted string,
         plaintext(or decrypted string), or the generated key string and
         and translates it based on the provided alpha dictionary.
         NOTE** all strings are converted to lowercase."""
        plaintext = str(e_d_string_or_key_string).lower()
        string_list = []
        for ch in plaintext:
            for k, v in self.alpha_dictionary.items():
                if ch in v:
                    string_list.append(k)
                else:
                    continue
        return string_list

    def key_generator(self, standard_string_length):
        """Generates a random list of letters that is equal to
        the length of the provided string.  The list is based on on the
        key_values variable below, which is
        a list if ascii values"""
        string_length = len(standard_string_length)
        key_list = []
        key_values = [32, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111,112,
                      113, 114, 115, 116, 117, 118, 119, 120, 121, 122]

        for i in xrange(string_length):
            key_list.append(chr(choice(key_values)))
        with open("key.dat", 'w') as data:
            temp_string = ""
            for key in key_list:
                temp_string += key
            data.write(temp_string)
        return self.string_converter("".join(key_list))

    def encrypt_file(self, zip_password):
        """Encrypts the key.dat file with a zip encryption using pyminizip.
        For more instructions regarding pyminizip you visit pypi.python.org
        and search for the module."""
        pyminizip.compress("key.dat", "key.zip", zip_password, int(9))
        os.remove("key.dat")

    def decrypt_file(self, zip_password):
        """Unzips key.zip file using a supplied password"""
        zipfile.ZipFile("key.zip").extractall(pwd=zip_password)

    def decrypt_string(self, key, encrypted_string, key_file_mode=False, encrypted_string_file_mode=False):
        """Method that takes either the key or the encrypted string as a
        string or can the key and encrypted string a as file and decrypts
        the string using the provided string. NOTE** The key provided must
        be the same key used to encrypt the string, in order to use the the key.dat file
        you must first also be able to unzip it using a password."""
        if key_file_mode is True:
            self.my_key = key
            with open(self.my_key, 'r') as key_data:
                self.my_key = key_data.read()
        else:
            self.my_key = key
        if encrypted_string_file_mode is True:
            self.my_string = encrypted_string
            with open(self.my_string, 'r') as string_data:
                self.my_string = string_data.read()
        else:
            self.my_string = encrypted_string

        my_string_num_list = self.string_converter(self.my_string)
        my_key_num_list = self.string_converter(self.my_key)

        combined_list_values = []
        for j in xrange(len(my_string_num_list)):
            combined_list_values.append(my_string_num_list[j] - my_key_num_list[j])

        decrypted_list = [k % 27 for k in combined_list_values]

        message = []
        for num in decrypted_list:
            for k, v in self.alpha_dictionary.items():
                if k == num:
                    message.append(str(v))
        decrypted_string = "".join(message).replace("[", "").replace("]", "").replace("'", "")
        with open("decrypted_message.txt", 'w') as message:
            message.write(decrypted_string)
        return decrypted_string

    def encrypt_string(self, plain_text, string_file_mode=False):
        """Method that takes either the key or the plaintext as a
        string or can the key and plaintext a as file and encrypts it
        using the randomly generated key"""

        if string_file_mode is True:
            with open(plain_text) as plaintext_data:
                self.file_data = str(plaintext_data.read())
                self.string_list = self.file_data
        else:
            self.string_list = plain_text

        self.string_list = self.string_converter(self.file_data)
        self.key_list = self.key_generator(self.file_data)

        combined_list_values = []

        for j in xrange(len(self.string_list)):
            combined_list_values.append(self.string_list[j] + self.key_list[j])

        encrypted_list = [k % 27 for k in combined_list_values]

        message = []
        for num in encrypted_list:
            for k, v in self.alpha_dictionary.items():
                if k == num:
                    message.append(str(v))
        encrypted_string = "".join(message).replace("[", "").replace("]", "").replace("'", "")
        with open("encrypted_message.txt", 'w') as message:
            message.write(encrypted_string)

        self.encrypt_file(raw_input("Please type in a password to zip and encrypt the key.dat file\n"))

        return encrypted_string

#Example of use
ope = OneTimePadEncryption()
#print ope.encrypt_string("this is a test")
print ope.encrypt_string("pad_plaintext.txt", string_file_mode=True)
ope.decrypt_file("password")
print ope.decrypt_string("key.dat", "encrypted_message.txt", key_file_mode=True, encrypted_string_file_mode=True)
