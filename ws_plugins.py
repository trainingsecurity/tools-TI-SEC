#!/usr/bin/python3
# _*_ coding: utf-8 _*_

import argparse
import sys
from os import path
import os
import requests
from progress.bar import Bar
from datetime import datetime

print("")
os.system('apt install figlet')
os.system('apt install lolcat')
os.system('wget https://raw.githubusercontent.com/hypn/custom-wordlists/master/wordpress-popular-plugins.txt')
os.system('clear')


parser = argparse.ArgumentParser()
parser.add_argument('-u','--url',help="Enter the url")
parser = parser.parse_args()


def main():
	if parser.url:
		os.system("figlet -c WP_Plugins.py | lolcat")
		if path.exists('wordpress-popular-plugins.txt'):
			print("")
			print("="*40)
			print("    Date: " + str(datetime.now()))
			print("="*40)
			wordlist_plugins_wp = open('wordpress-popular-plugins.txt')
			wordlist_plugins_wp = wordlist_plugins_wp.read().split('\n')
			url_target = parser.url
			component = "/wp-content/plugins/"
			list_plugins_wp = []
			print("")
			bar_load = Bar('Loading...',max=len(wordlist_plugins_wp))
			for plugin in wordlist_plugins_wp:
				bar_load.next()
				try:
					petition_plugin_search = requests.get(url=url_target+component+plugin)
					if petition_plugin_search.status_code == 200:
						found_plugin = url_target+component+plugin
						list_plugins_wp.append(found_plugin.split('\n')[-1])
				except:
					pass
			bar_load.finish()
			for plugin in list_plugins_wp:
				print(f"Plugin Found => {plugin}")
		else:
			os.system("wget https://raw.githubusercontent.com/hypn/custom-wordlists/master/wordpress-popular-plugins.txt")
			print("Run again")
	else:
		print("\n    The url has not been defined")
		print("    Usage: python3 ws_plugins.py -u/--url <url host>")


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print("Good bye")
		sys.exit()
