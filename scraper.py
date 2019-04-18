#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup

def fetch_url():
	r=requests.get('https://online.justice.vic.gov.au/wwccu/checkstatus.doj')
	return r.text

soup = BeautifulSoup(fetch_url(), 'html.parser')


print(soup.title.string)
