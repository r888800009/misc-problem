#!/usr/bin/env python
import re
import hashlib

import string
from itertools import product

print('gen validator')  
print(len(string.printable))
prod2 = product(string.printable, repeat=2)
prod3 = product(string.printable, repeat=3)
mapping = {}
count = 0
for i in list(prod2) + list(string.printable) + list(prod3):
    three_bytes = ''.join(i)
    mapping[str(hashlib.md5(bytes(three_bytes, 'ascii')).hexdigest())] = three_bytes
    count += 1
print(count)

question = input('> ')

# check question verified
regex = r'[a-zA-Z/:0-9.]{1,3}'

print('''The message was divided into multiple parts,
each of which is three bytes (or one or two) long,
and then every three bytes (or one or two) has been hashed by md5.\n''')

print('for example, "aa" is')
print(hashlib.md5(b'aa').hexdigest())
print('')

print(f'each part matches this regex {regex}\n')

print('Message md5:')
for a in range(0,len(question), 3):
    three_bytes = question[a+0:a+3]
    #print(three_bytes)
    assert re.fullmatch(regex, three_bytes), 'valid question'
    print(hashlib.md5(bytes(three_bytes, 'ascii')).hexdigest())

print('\n\n\n')
print('validating')
for a in range(0,len(question), 3):
    three_bytes = question[a+0:a+3]
    hash1 = hashlib.md5(bytes(three_bytes, 'ascii')).hexdigest() 
    print(mapping[str(hash1)])


