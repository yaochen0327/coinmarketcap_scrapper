from bs4 import BeautifulSoup
import os
import pandas as pd
import glob

if not os.path.exists("parsed_flies"):
	os.mkdir("parsed_flies") 

df = pd.DataFrame()

for one_file_name in glob.glob("html_flies/*.html"): #glob will loop through all of the files in the selected folder

	print("parsing: ",one_file_name)
	scraping_time = os.path.basename(one_file_name).replace("coinmarketcap","") 
	#f = open("html_flies/coinmarketcap20200129190530.html", "r") #"r" instead of "wb", read the file
	f = open(one_file_name, "r")
	#html_content = f.read()
	#print(html_content)
	soup = BeautifulSoup(f.read(), 'html.parser')

	f.close()
	#print(soup)

	currencies_table = soup.find("tbody") #STEP 1: get to the table, using the unique keyword

	currencies_rows = currencies_table. find_all("tr") #STEP 2: find tr to get to the row
	for r in currencies_rows: #loop through all the rows
		currency_price = r.find("td", {"class":"cmc-table__cell--sort-by__price"}).find("a").text  #STEP 3: locate the cell we want by the unique keyword element form "class". i.e., #<td class="cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__price"><a href="/currencies/bitcoin/markets/" class="cmc-link">$9,542.93</a></td>
		currency_name = r.find("td", {"class":"cmc-table__cell--sort-by__name"}).find("a",{"class":"cmc-link"}).text
		currency_marketcap = r.find("td", {"class":"cmc-table__cell--sort-by__market-cap"}).find("div").text
		currency_supply = r.find("td", {"class":"cmc-table__cell--sort-by__circulating-supply"}).find("div").text.replace("*","")
		currency_link = r.find("td", {"class":"cmc-table__cell--sort-by__name"}).find("a",{"class":"cmc-link"})["href"]

		# print(currency_name)
		# print(currency_price)
		# print(currency_marketcap)
		# print(currency_supply)
		df = df.append({
			'time':scraping_time,
			'name': currency_name,
			'price': currency_price,
			'marketcap': currency_marketcap,
			'supply': currency_supply,
			'link': currency_link
			}, ignore_index=True)

	#currencies_row = currencies_table. find("tr") #STEP 2: find tr to get to the row
	# currency_price = currencies_row.find("td", {"class":"cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__price"}).find("a").text  #STEP 3: locate the cell we want by the unique keyword element form "class". i.e., #<td class="cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__price"><a href="/currencies/bitcoin/markets/" class="cmc-link">$9,542.93</a></td>
	# currency_name = currencies_row.find("td", {"class":"cmc-table__cell cmc-table__cell--sticky cmc-table__cell--sortable cmc-table__cell--left cmc-table__cell--sort-by__name"}).find("a",{"class":"cmc-link"}).text
	# currency_marketcap = currencies_row.find("td", {"class":"cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__market-cap"}).find("div").text
	# currency_supply = currencies_row.find("td", {"class":"cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__circulating-supply"}).find("div").text

	df.to_csv("parsed_flies/coinmarketcap_dataset.csv") #use panda to transfer it into .csv data

	#add one more column o .csv file to in dicate the date/time of the original file






