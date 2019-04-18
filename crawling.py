#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
response ={}

def vic_verify(cardnumber, lastname):

	cardnumber = cardnumber
	lastname = lastname

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
				
				if "is current" in message:
					response = {
						"result": "valid",
						"message": message
						}
					print(response)
					#to-do: extract expiry date from response
				
				else:
					response = {
						"result": "error",
						"message": "Something went wrong."
					}
					print(response)

			except:
				elem_mismatch = driver.find_element_by_class_name("error")
				if elem_mismatch:
					response = {
						"result" : "error",
						"message" : "Something unknown happened, perhaps check the input details and try again"
					}
					print(response)
				else:
					response = {
						"result" : "error",
						"message" : elem_mismatch.text
					}
					print(response)
				#to-do: develop better error handling here, as there are different potential responses 
		except:
			print('Something unknown happened.')
	except:
		response = {
			'result': 'error', 
			'message': "Could not retrieve the URL provided"
			}
		print(response)

	return response 


vic_verify("1573624A-01", "byrne")
