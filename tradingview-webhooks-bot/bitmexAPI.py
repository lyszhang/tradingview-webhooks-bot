import bitmex
import json


class BitmexClient(object):
    def __init__(self, key, secret, test=True):
        self.client = bitmex.bitmex(test, key, secret)

    def place_order(self, action='buy', currency='XBTUSD', amount=0):
        orders_numb = amount if action == 'buy' else -amount
        order = self.client.Order.Order_new(symbol=currency, orderQty=orders_numb).result()
        print(order)
        return order

    def get_orderbook(self, currency='XBTUSD', depth=20):
        orderbook = self.client.OrderBook.OrderBook_getL2(symbol=currency, depth=depth).result()
        print(orderbook)
        return orderbook

    def get_selforder(self, currency='XBTUSD', reverse=True):
        orders = self.client.Order.Order_getOrders(symbol=currency, reverse=reverse).result()
        print(orders)
        return orders

    def get_position(self, currency='XBTUSD'):
        position = self.client.Position.Position_get(filter=json.dumps({'symbol': currency})).result()
        print(position)
        return position

    def cancel_order(self, orderID):
        canceled_order = self.client.Order.Order_cancel(orderID=orderID).result()
        print(canceled_order)
        return canceled_order

    def cancel_allorder(self, symbol='XBTUSD'):
        canceled_order = self.client.Order.Order_cancelAll(symbol=symbol).result()
        print(canceled_order)
        return canceled_order


