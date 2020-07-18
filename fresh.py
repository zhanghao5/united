from united_air import FlightSearch
import time



date_list = ["07/18/2020","07/22/2020","07/25/2020","07/29/2020", 
			  "08/01/2020", "08/05/2020","08/12/2020","08/1501/2020","08/19/2020","08/22/2020", "08/26/2020", "08/29/2020"]


while True:
	for date in date_list:
		test = FlightSearch()
		test.search_flight(date)
		test.close_web()
		del test
		time.sleep(10)
	
	time.sleep(900)

# single test case successful

test = FlightSearch()
test.search_flight("11/18/2020")
test.close_web()
del test

