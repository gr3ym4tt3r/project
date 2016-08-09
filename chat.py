#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime

def loggingIn():
    url = 'http://forum.top-hat-sec.com/index.php?action=login'
    browser = webdriver.Firefox()
    browser.get(url)
    browser.find_element_by_name('user').send_keys('username')
    browser.find_element_by_name('passwrd').send_keys('password')
    browser.find_element_by_id('frmLogin').submit()
    browser.find_element_by_id('shoutbox_message').send_keys(
        '/me minion says he is sending this message on {}. Fuck yea'.format(
            datetime.now()), Keys.ENTER
    )
    WebDriverWait(browser, 2)
    browser.close()

loggingIn()
