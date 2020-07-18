import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as action
import time
import os

import smtplib
from email.mime.multipart import MIMEMultipart

class FlightSearch():
	def __init__(self):
		'''
			setup chrome driver
		'''
		self.PATH = "/home/hao/Code/chromedriver"
		self.chrome_options = webdriver.ChromeOptions()
		self.chrome_options.add_argument('-incognito')
		self.driver = webdriver.Chrome(self.PATH, options=self.chrome_options)
		# setup email
		self.server = smtplib.SMTP('smtp.outlook.com', 587)

	def __del__(self):
		print("deleting instance")

	def connect_server(self):
		# username and src email hardcoded
		
		self.server.ehlo()
		self.server.starttls()
		# change with your sending email and passwd
		self.server.login("taotaomaggie@hotmail.com", "passwd")

	def open_United(self):
		self.driver.get("https://www.united.com/en/us")
		self.driver.maximize_window()
		print("Open main page successfully")


	def test_src_dst(self):
		# self.open_United()
		driver = self.driver
		time.sleep(2)
	
		# fill in src and dest airport in my case sfo and pvg
		try:
			src_airport = driver.find_element_by_id('bookFlightOriginInput')
			time.sleep(2)
			src_airport.send_keys(Keys.CONTROL, "a", Keys.BACKSPACE)
			print("Departing Airport input field has been clicked successfully.")
			time.sleep(2)
			action(driver).move_to_element(src_airport).send_keys("San Francisco").perform()
			time.sleep(2)
		except Exception as err:
			print(str(err))

		try:
			dst_airport = driver.find_element_by_id("bookFlightDestinationInput")
			# dst_airport.click()
			time.sleep(2)
			dst_airport.click()
			time.sleep(1)
			print("Destination airport has been clicked successfully. ")
			action(driver).move_to_element(dst_airport).send_keys("Shanghai").perform()
			time.sleep(3)
		except Exception as err:
			print(str(err))

	def test_oneway_date(self, date_str):
		# self.open_United()
		driver = self.driver
		time.sleep(2)

		try:
			oneway = driver.find_element_by_id("oneway")
			oneway.click()
			print("Oneway Radio button has benn clicked successfully.")
		except Excepton as err:
			print(str(err))
		
		driver.find_element_by_id("DepartDate").clear()
		date = driver.find_element_by_id("DepartDate")
		time.sleep(1)
		date.click()
		date.send_keys(Keys.END)
		for i in range(11):
			date.send_keys(Keys.BACKSPACE)
		time.sleep(2)
		date.send_keys(date_str)
		time.sleep(3)



	def test_num(self):
		# self.open_United()
		driver = self.driver
		time.sleep(2)
		# number of travellers
		try:
			travelers = driver.find_element_by_id('bookFlightModel.passengers')
			action(driver).move_to_element(travelers).click().perform()
			print('main travelers clicked successfully')
		except Exception as err:
			print(str(err))

		time.sleep(2)
		try:
			peo = driver.find_element_by_id("NumOfAdults plusBtn")
			n(driver).move_to_element(peo).click().perform()
			print('Increased one adult traveler.')
		except Exception as err:
			print(str(err))
		time.sleep(2)

	def test_search_btn(self):
		# self.open_United()
		driver = self.driver
		time.sleep(2)

		search = driver.find_element_by_xpath("//button[@aria-label='Find flights']")
		search.click()
		time.sleep(15)

	def search_flight(self, date_str):
		self.open_United();
		self.test_oneway_date(date_str)
		self.test_src_dst()
		# self.test_num()
		self.test_search_btn()
		time.sleep(10)
		
		if "13h 30m" in self.driver.page_source:
			print("non stop find ......")
			# play sound
			dur = 6
			freq = 440
			os.system('play -nq -t alsa synth {} sine {}'.format(dur, freq))
			# play sound windows import winsound
			# dur = 6
			# freq = 440
			# winsound.Beep(freq, dur)

			# email_msg = "Non_stop flight on " + date_str
			# # self.connect_server()
			# # self.send_mail(email_msg)

	def send_mail(self, msg):
		send_msg = "\r\n".join([
			"From: taotaomaggie@hotmail.com",
			"To: bnuepzhd@gmail.com",
			"Subject: flight_ticket_reminder!!!",
			"",
			msg
			])
		self.server.sendmail('taotaomaggie@hotmail.com', 'bnuepzhd@gmail.com', send_msg)
		self.server.sendmail('taotaomaggie@hotmail.com', 'zwz631108@sina.com', send_msg)


	def close_web(self):
		self.driver.quit()
