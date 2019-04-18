# wwcc-api
WWCC-API

## about this project 

This project has been created in order to offer an API that allows us to verify a working with children or vulnerable peoples check within each state of Australia. Noting it is not possible to integrate with two states in Australia at present: ACT does not offer (or require) digital verification, and South Australia are implementing a new system to be launched on 1 July 2019.


The API will be implemented in three parts:

### Part One

Victoria, Queensland, and Western Australia offer unrestricted, public web forms that can be used to verify a WWC/VP credential. Part one will implement a basic API that takes the required inputs to these forms, and uses a headless web crawler to complete the forms and scrape the result before being passed back via the API.

### Part Two 
Tasmania and Northern Territory offer publicly accessible web forms, but these forms are protected with basic CAPTCHA. Part two will integrate a CAPTCHA service so that we can still complete the verification check.

### Part Three
New South Wales offers a verification service, but the form is protected by reCAPTCHA and is behind an authentication wall. Part Three will introduce the ability for the headless browser to authenticate to the NSW website using login details provided by the user, before using tools similar to part one and two to complete the verification check.

# Local installation of this project

This project uses Python 3.7.3 Flask to run a light weight API. 
Installing on your local machine is relatively straight forward. 

Recommended: Have a virtualenv for this project installed and active

Steps to install: '
 * Clone repository'
 * Activate your python virtualenv (optional, but recommended)
 * install dependencies using run 'pip install -r requirements.txt'
 * run API local / development server using 'FLASK_APP=hello.py flask run'
 * run the WWCC Victoria verification API using ./crawling.py
