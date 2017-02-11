import requests, re, gi
from datetime import datetime
gi.require_version('Notify', '0.7')
from gi.repository import Notify
try:
    # from twilio.rest import TwilioRestClient
    from bs4 import BeautifulSoup
except ImportError as error:
    print('[!] EiP Overwritten with Gay Porn: {}'.format(error))

account_sid = ''
auth_token = ''

# mdKey from your email will go right hurr
mdKey = ''
now = datetime.now()
mon = now.month
nex = mon+1
datumKey = '1-{}-2017'.format(mon)
datunKey = '1-{}-2017'.format(nex)
dateList = ''
payload = {'md':mdKey, 'datum' :datumKey}
payload2 = {'md' :mdKey, 'datum' :datunKey} 

def writingData(filename, datelist):
    with open(filename, 'w') as file:
        file.write(datelist)

def readingData(calenDateFile):
    with open(calenDateFile, 'r') as file:
        return set(file)

def desktopNotification(message):
    Notify.init('script')
    Notify.Notification.new('Available dates', message).show()

def sendText(message):
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    client.messages.create(
        to='',          # Your number
        from_='',       # Your Twilio number
        body='Good news! {} is now available! Book now before time runs out!')

print('[+] Gathering dates')
resp = requests.get('https://www.offensive-security.com/exam.php', params=payload)
soup = BeautifulSoup(resp.content, 'lxml')
resp2 = requests.get('https://www.offensive-security.com/exam.php', params=payload2)
soup2 = BeautifulSoup(resp2.content, 'lxml')
for link in soup.findAll('a', href=True):
    if 'exam' in link['href']:
        date = re.search(r'\d{4}-\d{2}-\d{2}', link['href']).group()
        date = datetime.strptime(date, '%Y-%m-%d').strftime('%B %d, %Y')
        dateList += '{}\n'.format(date)

writingData('available.txt', dateList)
desktopNotification(dateList)
