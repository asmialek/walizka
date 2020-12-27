import codecs
password = input('Type in new password (without polish letters): ')

with open('cipher', 'w') as f:
    f.write(codecs.encode(password, 'rot13'))

print(f'Password "{password}" was created and encoded in "cipher" file using ROT13 cipher.')