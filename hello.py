from flask import Flask
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def hello():
	try:
		r=requests.get('https://online.justice.vic.gov.au/wwccu/checkstatus.doj')
		soup = BeautifulSoup(r.text, 'html.parser')
		return "Found: %s" % soup.title.string
	except:
		return "Something went wrong"