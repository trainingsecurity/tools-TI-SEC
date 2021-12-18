#!/usr/bin/python
# _*_ coding: utf-8 _*_

import argparse
import requests
import sys
from bs4 import BeautifulSoup
import os
from datetime import datetime


parser = argparse.ArgumentParser()
parser.add_argument('-u','--url',help='Enter the url')
parser = parser.parse_args()


os.system('apt install lolcat -y')
os.system('apt install figlet -y')
os.system('clear')
print("")


os.system('figlet -c WS_Themes.py | lolcat -a')

def main():
	if parser.url:
		url_target = parser.url
		petition = requests.get(url=url_target)
		parsed = BeautifulSoup(petition.text,'html5lib')
		print("")
		print("="*30)
		print(" ", datetime.now())
		print("="*30)
		print("+"*49)
		print(f"\n  Themes Found in {parser.url}:\n")
		print('+'*49)
		print("")
		for prd in parsed.find_all('link'):
			if '/wp-content/themes' in prd.get('href'):
				themes = prd.get('href')
				themes = themes.split('/')
				if 'themes' in themes:
					theme_position = themes.index('themes')
					theme = themes[theme_position+1]
					print(f"    Theme => {theme}")
	else:
		print('\nEnter the url')
		print('Usage: python3 ws_themes.py -u/--url <url>')


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print("Good Bye")
		sys.exit()

