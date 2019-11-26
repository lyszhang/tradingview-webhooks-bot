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


def send_order(data):

    """
    This function sends the order to the exchange using ccxt.
    :param data: python dict, with keys as the API parameters.
    :return: the response from the exchange.
    """

    # Replace kraken with your exchange of choice.
    exchange = ccxt.kraken({
        # Inset your API key and secrets for exchange in question.
        'apiKey': '',
        'secret': '',
        'enableRateLimit': True,
    })

    # Send the order to the exchange, using the values from the tradingview alert.
    print('Sending:', data['symbol'], data['type'], data['side'], data['amount'], calc_price(data['price']))
    order = exchange.create_order(data['symbol'], data['type'], data['side'], data['amount'], calc_price(data['price']))
    # This is the last step, the response from the exchange will tell us if it made it and what errors pop up if not.
    print('Exchange Response:', order)


def bitmex_order(data):
    client = bitmex.bitmex(test=False,
                           api_key="wBjcgxQfLBBTgSzaKtJCDh0E",
                           api_secret="CX543A3hE1oHj_O19u_nxouCCuwDK71VB3nDqMJxpPJzLBQC")
    result = client.Instrument.Instrument_get(filter=json.dumps({'symbol': 'XBTJPY'})).result()
    print("order res", result)