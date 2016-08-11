#!/usr/bin/env python

################################################################
# Chase Miller
# chasemiller.me
#
# This script scrapes your steam library and compares it against
# a local-multiplayer game database to quickly identifiy which
# steam games in your library are local multiplayer capable.
# 
# Get your Steam API key: https://steamcommunity.com/devs
# Get your 64-bit Steam ID: https://steamid.io/
#
# Local multiplayer games scraped from: 
# http://pcgamingwiki.com/wiki/List_of_Local_Multiplayer_Games
# Thanks to Nicereddy for compiling the original list!
################################################################

import sys 
import json
import requests
from lxml import html
from urllib2 import urlopen

reload(sys)  
sys.setdefaultencoding('utf8')

apikey = '' # Enter your 64-bit APID here
steamid = '' # Enter your Steam ID here
page = requests.get('http://pcgamingwiki.com/wiki/List_of_Local_Multiplayer_Games')
tree = html.fromstring(page.content)

def get_owned_games(apikey, steamid):
    url = ('http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/'
           '?key={}&steamid={}&include_appinfo=1'.format(apikey, steamid))

    return json.loads(urlopen(url).read().decode())['response']['games']

def compare_games():
	owned_games = str(get_owned_games(apikey, steamid))
	multiplayer_games = tree.xpath('//table[@class="wikitable sortable"]//tr/td/a/@title')

	for game in multiplayer_games:
		if game in owned_games:
			print game

def main():
	compare_games()

if __name__ == "__main__":
    main()