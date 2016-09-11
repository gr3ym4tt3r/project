from random import sample

char = []

def chars():
    for x in range(0x21, 0x7f):
        char.append('{:02x}'.format(x))

def zeroEAX():
    while True:
        value = int(''.join(sample(char, 4)), 16)
        value2 = int(''.join(sample(char, 4)), 16)
        if value & value2 == 0:
            return value, value2

chars()
print('[+] Quick way to zero out EAX')
while True:
    for values in zeroEAX():
        print('\tAND EAX, {:08x}'.format(values))
    break
