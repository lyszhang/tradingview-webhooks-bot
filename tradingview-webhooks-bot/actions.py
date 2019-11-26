import ccxt
import ast
import json
import bitmex

def parse_webhook(webhook_data):

    """
    This function takes the string from tradingview and turns it into a python dict.
    :param webhook_data: POST data from tradingview, as a string.
    :return: Dictionary version of string.
    """
    text = json.loads(webhook_data)
    return text


def calc_price(given_price):

    """
    Will use this function to calculate the price for limit orders.
    :return: calculated limit price
    """

    if given_price == None:
        price = given_price
    else:
        price = given_price
    return price


def bitmex_order(data):
    client = bitmex.bitmex(test=False,
                           api_key="wBjcgxQfLBBTgSzaKtJCDh0E",
                           api_secret="CX543A3hE1oHj_O19u_nxouCCuwDK71VB3nDqMJxpPJzLBQC")
    orderbook = client.OrderBook.OrderBook_getL2(symbol='XBTUSD', depth=20).result()
    print("order res", orderbook)