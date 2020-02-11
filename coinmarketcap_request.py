###basic scrap and save it into a file 

# import urllib.request

# f = open("coinmarketcap.html", "wb") #save the .html file

# response = urllib.request.urlopen('https://coinmarketcap.com/') #do the respuert
# print(response) #we get "<http.client.HTTPResponse object at 0x107dd1a60>", which is not wierd.. next, we need to read
# html = response.read()
# #print(html)

# f.write(html)
# f.close()


###basic scrap and save it into a file, which is doing the same thing as save the website as .html file


##scrape it reapeatedly
import urllib.request
import time
import datetime
import os
import random

if not os.path.exists("html_flies"):
	os.mkdir("html_flies") #store all the .html file seperately in another folder

for i in range(1):
	#f = open("coinmarketcap" + stri(i) + ".html", "wb") #save the .html file and uodate the file name (METHOD 1)
	current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
	##time stamp: short, readable, the same length:
	##2020 Jan 28 5:19:34 pm --> 20200128171934
	print(current_time_stamp)
	f = open("html_flies/coinmarketcap" + current_time_stamp + ".html", "wb")
	response = urllib.request.urlopen('https://coinmarketcap.com/') #do the resquest
	print(response)
	html = response.read()
#print(html)
	f.write(html)
	f.close()
	time.sleep(300 + random) #sleep for 300 seconds, 5-min interval
	#sleeptime=random.randint(1, 5) ##### try this way!!
	#time.sleep(sleeptime)

##scrape it reapeatedly



###parsing... next time




