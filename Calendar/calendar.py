import requests, sys, re
from datetime import datetime
try:
    from bs4 import BeautifulSoup
except ImportError as error:
    print('[!] Uh-oh: {}'.format(error))
    
# mdKey from your email will go right hurr
mdKey = ''
dateList = []
payload = {
    'md':mdKey
}

print('[+] Gathering dates')
response = requests.get('https://www.offensive-security.com/exam.php', params=payload)

soup = BeautifulSoup(response.content, 'lxml')
print('[+] The following dates are available:')
for link in soup.findAll('a', href=True):
    if 'exam' in link['href']:
        date = re.search(r'\d{4}-\d{2}-\d{2}', link['href']).group()
        date = datetime.strptime(date, '%Y-%m-%d').strftime('%B %d, %Y')
        dateList.append(date)
        print('\t{}'.format(date))
