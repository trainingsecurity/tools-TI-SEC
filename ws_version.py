#!/usr/bin/python3
# _*_ coding: utf-8 _*_

import requests
import argparse
from bs4 import BeautifulSoup
import sys
import os
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('-u','--url',help='Enter the url')
parser = parser.parse_args()


print("")

os.system('apt install lolcat -y')
os.system('apt install figlet -y')
os.system('clear')

def main():
	if parser.url:
		print("")
		os.system("figlet -c WS_Version.py | lolcat -a")
		print("")
		print("="*34)
		print(" Date: " + str(datetime.now()))
		print("="*34)
		print("")
		print("+"*11)
		print(" Versiones")
		print("+"*11)
		url_target = parser.url
		petition = requests.get(url=url_target)
		parsed = BeautifulSoup(petition.text,'html5lib')
		for x in parsed.find_all('meta'):
			if x.get('name') == 'generator':
				wordpress_version = x.get('content')
				print(wordpress_version)
	else:
		print("Enter the url")
		print("Usage: python3 ws.py -u <url>")


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print("Good Bye")
		sys.exit()
