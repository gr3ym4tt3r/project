#!/usr/bin/python

from requests import get
from bs4 import BeautifulSoup
from os import path, makedirs, chdir
from sys import exit

def downloadPdf(pdfPath):
    pdfs = get('https://media.defcon.org/DEF CON 24/DEF CON 24 presentations/{}'.format(pdfPath), stream=True)
    with open(pdfPath, 'wb') as file:
        file.write(pdfs.content)

if __name__ == '__main__':
    request = get('https://media.defcon.org/DEF CON 24/DEF CON 24 presentations/')
    soup = BeautifulSoup(request.content, 'html.parser')
    print('[+] Creating DefConPdfs Directory...')
    try:
        if not path.isdir('DefConPdfs'):
            makedirs('DefConPdfs')
    except OSError as error:
        print('[!] Uh-oh! {}'.format(error))
        exit()
    chdir('DefConPdfs')
    for links in soup.find_all('a'):
        if 'pdf' in links.text:
            print('[+] Saving: {}'.format(links.text))
            downloadPdf(links.text)
