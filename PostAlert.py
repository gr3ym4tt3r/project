from __future__ import print_function
from requests import get
from bs4 import BeautifulSoup
from hashlib import md5
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

payload = {
    'action' : '.xml',
    'type' : 'rss'
}

def loggingIn(f):
    url = 'http://forum.top-hat-sec.com/index.php?action=login'
    browser = webdriver.Firefox()
    browser.get(url)
    browser.find_element_by_name('user').send_keys('username')
    browser.find_element_by_name('passwrd').send_keys('password')
    browser.find_element_by_id('frmLogin').submit()
    browser.find_element_by_id('shoutbox_message').send_keys(f, Keys.ENTER)
    sleep(2)
    browser.close()

def postchecking():
    for title in soup.findAll('title')[1:2]:
        for message in soup.findAll('description')[1:2]:
            for link in soup.findAll('link')[1:2]:
                for category in soup.findAll('category')[0:1]:
                    responseMessage = '/me minion: New post in response to {}! {}.. Click here to view: {}'.format(
                        title.text,
                        message.text.strip().replace('<br />', ' '),
                        link.text)
                    postMessage = '/me minion: {} was posted in {}! {}... Click here to view: {}'.format(
                        title.text,
                        category.text,
                        message.text.strip().replace('<br />', ' '),
                        link.text)
                    if 'Re:' in title.text:
                        loggingIn(responseMessage)
                    else:
                        loggingIn(postMessage)

def hashed(x):
    return md5(x.content).hexdigest()

if __name__ == "__main__":
    print('[+] Checking Top Hat...\n[+] Ctrl+C to exit')
    currentCheck = 'fca7c2f1ab797ba94a5c01e379fff033'
    try:
        while True:
            response = get('http://forum.top-hat-sec.com/index.php', params=payload)
            soup = BeautifulSoup(response.content, 'html.parser')
            if currentCheck == hashed(response):
                print('\t[+] There are no new posts!')
            else:
                print('\t[+] There\'s a new post!')
                currentCheck = hashed(response)
                print('\t\t[>] New hash: {}'.format(currentCheck))
                postchecking()
            sleep(900) # 900 is every 15 minutes
    except KeyboardInterrupt:
        print('[!] Exiting...')
