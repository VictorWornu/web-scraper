# http://quotes.toscrape.com

import requests 
from bs4 import BeautifulSoup
from csv import writer

# response = requests.get("http://quotes.toscrape.com")
# soup = BeautifulSoup(response.text, "html.parser")
# quotes = soup.find_all("quote")

# with open("first.csv", "w") as csv_file:
# 	csv_writer = writer(csv_file)
# 	csv_writer.writerow(["Writer", "Quote"])

# for quote in quotes:
# 		a_tag = article.find("a")
# 		title = a_tag.get_text()
# 		url = a_tag["href"]
# 		date = article.find("time")["datetime"]
# 		csv_writer.writerow([title, url, date])

print("Type your name and hit enter to get your daily quote")
name = input(" ")

response = requests.get("http://quotes.toscrape.com")
soup = BeautifulSoup(response.text, "html.parser")
quotes = soup.find_all("body")

for quote in quotes:
	overall = quote.find("div")
	daily_quote = overall.find("span").get_text()
	kuo = str(daily_quote)
	print(name + ", " + kuo)
	
	# print(quote.find("small").get_text())