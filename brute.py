import hashlib

lead = "soMe3FK2J+YFAMzUjwpfpA"
trail = "6dcKXY3x/JRZbyj9RDB/Lw"

bob_hash = 'b5406d12c28fe602b27b063a2c1231f9'

with open('passwords.txt', 'r') as f:
    pass_list = f.read().splitlines()

found = False
password = ''

for p in pass_list:
    print(f'trying {p}')
    string  = f'{lead}{p}{trail}'
    md5_hash = hashlib.md5(string.encode())
    if md5_hash.hexdigest() == bob_hash:
        found = True
        password = p
        print(f'Found! Bob\'s password is {p}')
        break

print(found)
