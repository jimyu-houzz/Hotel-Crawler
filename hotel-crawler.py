from selenium.webdriver import Safari

## RUN: safaridriver --enable
## to enable webdrive

driver = Safari()

# Hotel Name
# hotel_name = 'rich-sunshine-inn_2/hotel/taitung'
hotel_name = 'afternoon-resort/hotel/all/hualien'

# Dates
base = '2021-04-'
dates = ['02', '03', '04', '05', '06', '07', '08']

for i in range(len(dates)):

	checkIn = base + dates[i]

	# searching Agoda website
	url = f"https://www.agoda.com/zh-tw/{hotel_name}-tw.html?finalPriceView=1&isShowMobileAppPrice=false&cid=1841724&numberOfBedrooms=&familyMode=false&adults=2&children=0&rooms=1&maxRooms=0&checkIn={checkIn}&isCalendarCallout=false&childAges=&numberOfGuest=0&missingChildAges=false&travellerType=1&showReviewSubmissionEntry=false&currencyCode=TWD&isFreeOccSearch=false&tag=17ed1551-e315-e170-cbea-84d6083fc11a&los=1&searchrequestid=51b232b7-075d-46d2-b2aa-798a2fa99789"

	driver.get(url)

	assert "No results found." not in driver.page_source
	print(f"Searching for Room price on date: {checkIn}.")

	driver.implicitly_wait(3) # wait for the website to actually load to start finding elements

	try:
		# looking for the "MasterRoom_TitleName" tag
		room_names = driver.find_elements_by_class_name('MasterRoom__TitleName')
		if len(room_names) == 0:
			print(f"Room not found for date: {checkIn}")
		for rm in room_names:
			print(rm.text)

		prices = driver.find_elements_by_class_name('pd-price')
		for price in prices:
			print(price.text)
	
	except:
		print(f"Exception: Room not found for data: {checkIn}")

	print(f'Finished checking.\n')

driver.close()



