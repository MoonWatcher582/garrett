from bs4 import BeautifulSoup
import sys
import requests

def main():
	url = sys.argv[1]
	theCity = requests.get(url)
	gold = theCity.text

	blackjack = BeautifulSoup(gold)
	
	#body = blackjack.find('div',attrs={"class":"content-block content-block-body content-block-note content-block-bg"})
	#clearfixContainer = body.find('div',attrs={"class":"wrap-container clearfix"})
	#container = clearfixContainer.find('div',attrs={"class":"card-container"})
	#clearfix = container.find('div',attrs={"class":"clearfix"})
	cards = blackjack.findAll('div',class_='text', limit=2)
	print(cards)


	#for card in cards.findAll('div'):
	#	for side in card.findAll('div'):
	#		print (side.find('div',attrs={"class":"side side-text"}).find('div',attrs={"class":"text text-small"}))

if __name__ == '__main__':
	main()
