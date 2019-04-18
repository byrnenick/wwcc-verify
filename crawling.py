#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://online.justice.vic.gov.au/wwccu/checkstatus.doj")

elem_card_number = driver.find_element_by_name("cardnumber")
elem_card_number.send_keys("1573624A-01")

elem_surname = driver.find_element_by_name("lastname")
elem_surname.send_keys("Byrne")


driver.find_element_by_id("pageAction_submit").click();