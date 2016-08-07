from requests import get
from bs4 import BeautifulSoup
from hashlib import md5

payload = {
    'action' : '.xml',
    'type' : 'rss'
}

x = get('http://forum.top-hat-sec.com/index.php', params=payload)

firstCheck = '6ab7f8c4dcc588c17b73ec643343aa0b'

shit = md5(x.content).hexdigest()
print(shit)

if shit == firstCheck:
    print('There are no new posts')
else:
    print('There is a new post!')
    print('firstcheck is {}'.format(firstCheck))
    firstCheck = shit
    print('first check is now {}'.format(firstCheck))

print firstCheck

#print x.content

#soup = BeautifulSoup(x.content, 'html.parser')
#print soup.prettify()

