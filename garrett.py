from bs4 import BeautifulSoup
import sys

def main():
    blackjack = BeautifulSoup(open(sys.argv[1], 'r').read())

if __name__ == '__main__':
    main()