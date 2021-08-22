#!/usr/bin/env python
import re
import hashlib
from tqdm import tqdm

import string
from itertools import product

# print(string.printable)
charlist = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ./: ' 

print('gen validator')  
print(len(charlist))
prod2 = product(charlist, repeat=2)
prod3 = product(charlist, repeat=3)
mapping = {}

for i in tqdm(list(prod2) + list(charlist) + list(prod3)):
    four_bytes = bytes(''.join(i), 'ascii')
    index = int(hashlib.md5(four_bytes).hexdigest(), 16)
    mapping[index] = int.from_bytes(four_bytes, byteorder='little')

# clean memory
del prod2
del prod3

# prod4: count ~= len(prod3) * 66
# that only cost 2.12 GB memory 
# note: 18974736it [00:25, 758663.39it/s]
# if charlist size = 100
# than dict size > 100000000, memory cost too much cost 13 GB 

for i in tqdm(product(charlist, repeat=4)):
    four_bytes = bytes(''.join(i), 'ascii')
    index = int(hashlib.md5(four_bytes).hexdigest(), 16)
    mapping[index] = int.from_bytes(four_bytes, byteorder='little')
    del four_bytes

question = input('> ')

# check question verified
regex = r'[a-zA-Z/:0-9. ]{1,4}'

print('''The message was divided into multiple parts,
each of which is 4 bytes (last is 1 to 4 bytes) long,
and then each part has been hashed by md5.\n''')

print('for example, "aa" is')
print(hashlib.md5(b'aa').hexdigest())
print('')

print(f'each part matches this regex {regex}\n')

print('Message md5:')
for a in range(0,len(question), 4):
    four_bytes = question[a+0:a+4]
    #print(four_bytes)
    assert re.fullmatch(regex, four_bytes), 'valid question'
    print(hashlib.md5(bytes(four_bytes, 'ascii')).hexdigest())

print('\n\n\n')
print('validating')
for a in range(0,len(question), 4):
    four_bytes = bytes(question[a+0:a+4], 'ascii')
    index = int(hashlib.md5(four_bytes).hexdigest(), 16)

    key2value = (mapping[index]).to_bytes(4, byteorder="little")

    print(key2value.decode("ascii").split('\x00')[0])

