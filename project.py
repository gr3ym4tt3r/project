from requests import get
from bs4 import BeautifulSoup
from hashlib import md5

payload = {
    'action' : '.xml',
    'type' : 'rss'
}

x = get('http://forum.top-hat-sec.com/index.php', params=payload)

currentCheck = 'ad7203dce871c23c6d8c1d462276f350'

shit = md5(x.content).hexdigest() # works

if shit == firstCheck:
    print('There are no new posts')
else:
    print('There is a new post!')
    # print('firstcheck is {}'.format(firstCheck)) works
    firstCheck = shit
    # print('first check is now {}'.format(firstCheck)) works

print firstCheck

soup = BeautifulSoup(x.content, 'html.parser')

## print the links to be able to click and view
currentLinks = []
for links in soup.findAll('link')[1:]:
    currentLinks.append(links)
if links in currentLinks:
    print('[+] New post! Click here to view: {}'.format(links.text))
#print(currentLinks)
#print(len(currentLinks))

## print whats being done to get a quick summary
currentPost = []
for posts in soup.findAll('title')[1:]:
    currentPost.append(posts)

## a new member??
currentCategories = []
for category in soup.findAll('category'):
    currentCategories.append(category)
#if x == 'Members Introduction':
#    print new member! ## something like this
#    print welcoming member message ##

print('[+] New post posted in {}! {}. Click here to view: {}'.format(category.text, posts.text, links.text))
## ouput:
## [+] New post posted in Polls! How many use MOSH and how do you like it?. Click here to view: http://forum.top-hat-sec.com/index.php?topic=5677.msg45882#msg45882
