#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys


response ={}

#run this to test script verify("1573624A-01", "byrne")

'''three possible responses:
1. "Pass" - the details provided have been verified as valid by Vic WWCC
2. "Fail" - the details provided were true, but the WWCC is not valid <to do>
3. "Error" - something went wrong
'''


def verify(cardnumber, lastname):

	options = Options()
	options.headless = True
	driver = webdriver.Firefox(options=options)
	
	cardnumber = cardnumber
	lastname = lastname

	print("starting verify function")

	try:
		driver.get("https://online.justice.vic.gov.au/wwccu/checkstatus.doj")
		try: 
			elem_card_number = driver.find_element_by_name("cardnumber")
			elem_card_number.send_keys(cardnumber)

			elem_surname = driver.find_element_by_name("lastname")
			elem_surname.send_keys(lastname)

			driver.find_element_by_id("pageAction_submit").click();

			try:
				elem_success = driver.find_element_by_class_name("success")
				message = elem_success.text
				print(message)
				
				if "is current" in message:
					result = "Pass"
					message = message
					#to-do: extract expiry date from response
				
				else:
					result = "Error"
					message = "Something went wrong."

			except:
				elem_mismatch = driver.find_element_by_class_name("error")
				if elem_mismatch is None:
					result = "Error"
					message = "Please check that you have provided the correct input information and try again."

				else:
					result = "Error"
					message = elem_mismatch.text

				#to-do: develop better error handling here, as there are different potential responses 
		except:
			result = "Error"
			message = "Something unknown happened"

	except:
		result = "Error"
		message = "Could not retrieve the URL provided"


	response = {
		"result" : result,
		"message" : message
	}
	
	driver.close()
	
	return response 



#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys


response ={}

#run this to test script verify("1573624A-01", "byrne")

'''three possible responses:
1. "Pass" - the details provided have been verified as valid by Vic WWCC
2. "Fail" - the details provided were true, but the WWCC is not valid <to do>
3. "Error" - something went wrong
'''


def testing(cardnumber, lastname):

	options = Options()
	options.headless = True
	driver = webdriver.Firefox(options=options)
	
	cardnumber = cardnumber
	lastname = lastname

	print("starting verify function")


	driver.get("https://online.justice.vic.gov.au/wwccu/checkstatus.doj")
	
	elem_card_number = driver.find_element_by_name("cardnumber")
	elem_card_number.send_keys(cardnumber)

	elem_surname = driver.find_element_by_name("lastname")
	elem_surname.send_keys(lastname)

	driver.find_element_by_id("pageAction_submit").click();

	
	driver.close()
	
	return "Done"






