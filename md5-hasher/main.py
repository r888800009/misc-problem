#!/usr/bin/env python
import re
import hashlib

import string
from itertools import product

print('gen validator')  
print(len(string.printable))
prod = product(string.printable, repeat=2)
mapping = {}
count = 0
for i in list(prod) + list(string.printable):
    two_bytes = ''.join(i)
    mapping[str(hashlib.md5(bytes(two_bytes, 'ascii')).hexdigest())] = two_bytes
    count += 1
print(count)

question = input('> ')

# check question verified
regex = r'[a-zA-Z/:0-9.]{1,2}'

print('''The message was divided into multiple parts,
each of which is two bytes long,
and then every two bytes (or one) was hashed by md5.\n''')

print('for example, "aa" is')
print(hashlib.md5(b'aa').hexdigest())
print('')

print(f'Alphabet list {regex}\n')

print('Message md5:')
for a in range(0,len(question), 2):
    two_bytes = question[a+0:a+2]
    assert re.fullmatch(regex, two_bytes), 'valid question'
    #print(two_bytes)
    print(hashlib.md5(bytes(two_bytes, 'ascii')).hexdigest())

print('\n\n\n')
print('validating')
for a in range(0,len(question), 2):
    two_bytes = question[a+0:a+2]
    hash1 = hashlib.md5(bytes(two_bytes, 'ascii')).hexdigest() 
    print(mapping[str(hash1)])


