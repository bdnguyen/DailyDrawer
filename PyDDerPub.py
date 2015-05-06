#!/usr/bin/env python3

import sys, argparse
import requests
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument(
	'email', metavar='STR', type=str, help='enter email')
parser.add_argument(
	'password', metavar='STR', type=str, help='enter password')
args = parser.parse_args()


email = sys.argv[1]
password = sys.argv[2]
soldierID1 = 361075717
soldierID2 = 371523810

session = requests.Session()
URL = 'https://battlefield.play4free.com/en/user/login/'
r1 = session.get(URL)
soup = BeautifulSoup(r1.content)
csrftoken = soup.find(id="csrf_token")['value']
payload = {'mail' : email, 'password' : password, '_csrf_token' : csrftoken}

r2 = session.post(URL, data=payload)

if email=='your_email@some_mail.com':
	r3 = session.get('https://battlefield.play4free.com/en/draw/drawCard?personaId='+soldierID1+'&card=0&_csrf_token='+csrftoken)
else: r3 = session.get('https://battlefield.play4free.com/en/draw/drawCard?personaId='+soldierID2+'&card=0&_csrf_token='+csrftoken)

print('Request response: ' + str(r3.status_code))
print(r3.text)
