import urllib.request #?? command+shift+p
import os
import time
import pandas as pd

if not os.path.exists("deep_link_html"):
	os.mkdir("deep_link_html")


df = pd.read_csv("parsed_flies/coinmarketcap_dataset.csv")
#print(df)
for link in df['link']:
	filename = link.replace("/currencies/","").replace("/","")
	if os.path.exists("deep_link_html/" + filename + ".html"):
		print(filename + " exists")
	else:
		print("Downloading: " + filename)
		# os.mkdir("deep_link_html")
		f = open("deep_link_html/" + filename + ".html.temp", "wb")
		response = urllib.request.urlopen('https://coinmarketcap.com'+link)
		html = response.read()
		f.write(html)
		f.close()
		os.rename("deep_link_html/" + filename + ".html.temp", "deep_link_html/" + filename + ".html")
		time.sleep(15)

	
#	print('https://coinmarketcap.com' + link)



