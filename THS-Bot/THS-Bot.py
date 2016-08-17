from __future__ import print_function
from requests import get
from bs4 import BeautifulSoup
from hashlib import md5
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from twilio.rest import TwilioRestClient
from re import sub
from HTMLParser import HTMLParser

url = 'http://forum.top-hat-sec.com/index.php?action=login'

sid = ''
token = ''
client = TwilioRestClient(sid, token)

payload = {
    'action' : '.xml',
    'type' : 'rss'
}

numbers = [
    ''
]

def htmlStrippa(message):
    cleaned = sub('<(.*?)>', '', message).replace('&nbsp;', '')
    html = HTMLParser()
    return html.unescape(cleaned)

def textMessage(contact):
    for number in numbers:
        client.messages.create(
            to = number,
            from_ = '',
            body = contact)

def loggingIn(f):
    browser = webdriver.Firefox()
    browser.get(url)
    browser.find_element_by_name('user').send_keys('username')
    browser.find_element_by_name('passwrd').send_keys('password')
    browser.find_element_by_id('frmLogin').submit()
    browser.find_element_by_id('shoutbox_message').send_keys('/me minion: {}'.format(f), Keys.ENTER)
    sleep(2)
    browser.close()

def postchecking():
    for title in soup.findAll('title')[1:2]:
        for message in soup.findAll('description')[1:2]:
            for link in soup.findAll('link')[1:2]:
                for category in soup.findAll('category')[0:1]:
                    responseMessage = 'New post in response to {}! {}.. Click here to view: {}'.format(
                        title.text.replace('Re: ', ''),
                        message.text.strip(),
                        link.text)
                    postMessage = '{} was posted in {}! {}... Click here to view: {}'.format(
                        title.text,
                        category.text,
                        message.text.strip(),
                        link.text)
                    if 'Re:' in title.text:
                        cleaned = htmlStrippa(responseMessage)
                        loggingIn(cleaned)
                        textMessage(cleaned)
                    else:
                        cleaned = htmlStrippa(postMessage)
                        loggingIn(cleaned)
                        textMessage(cleaned)

def hashed(x):
    return md5(x.content).hexdigest()

if __name__ == "__main__":
    print('[+] Checking Top Hat...\n[+] Ctrl+C to exit')
    currentCheck = 'c6509c6213cee3552a019fad7fa3ae47'
    try:
        while True:
            response = get('http://forum.top-hat-sec.com/index.php', params = payload)
            soup = BeautifulSoup(response.content, 'html.parser')
            if currentCheck == hashed(response):
                print('\t[+] There are no new posts!')
            else:
                print('\t[+] There\'s a new post!')
                currentCheck = hashed(response)
                print('\t\t[>] New hash: {}'.format(currentCheck))
                postchecking()
            sleep(300)
    except KeyboardInterrupt:
        print('[!] Exiting...')
