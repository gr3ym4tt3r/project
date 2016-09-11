def twosComp(math):
    answer = 0xffffffff - int(math, 16) + 1
    return answer

while True:
    value = raw_input('[+] Assembling for: ')
    if value == 'exit':
        break
    else:
        print('\t{:08x}'.format(twosComp(value)))
