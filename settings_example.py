#!/usr/bin/env python
# -*- coding: utf-8 -*-

# rename this file to settings.py and enter the api keys for poloniex

polo_api_key = "super_rich_acounts_api_key"
polo_api_secret = "super_secret_top_secret"



# set my coin data
currency = "BTC"
my_coin = "ZEC"

# dust definitions
# Those variables should be adjusted for the coin. They may change az the volume and value of the coin changes.

# This is total BTC amount of the orders in the orderbook
dust_total = 5.5

# this is the order amount in coins to accept not dust
dust_amount = 50.0

# the spread that we like to trade
min_spread = 0.0002

# How much coin we may trade?
max_trading_amount = 3
