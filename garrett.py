from bs4 import BeautifulSoup
import sys
import requests

def main():
	url = sys.argv[1]
	theCity = requests.get(url)
	gold = theCity.text

	blackjack = BeautifulSoup(gold)
	
	cards = blackjack.find('div',attrs={"class":"content-block content-block-body content-block-note content-block-bg"}).find('div',attrs={"class":"wrap-container clearfix"}).find('div',attrs={"class":"card-container"}).find('div',attrs={"class":"clearfix"}).find('div',attrs={"class":"content-wrap"})
	for link in blackjack.find_all('a'):
		print link.get('href')

if __name__ == '__main__':
	main()
