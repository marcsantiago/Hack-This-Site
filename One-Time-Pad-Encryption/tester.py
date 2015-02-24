#!/usr/bin/env python2.7
from OneTimePadEncryption import *

otpe = OneTimePadEncryption()
otpe.encrypt_string_or_file("Hello World. Are you ready for this awesome test? However, lol.")
otpe.decrypt_file("helloworld")
print otpe.decrypt_string_or_file("key.dat", "encrypted_message.txt", key_file_mode=True, encrypted_string_file_mode=True)
