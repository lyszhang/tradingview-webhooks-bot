"""
Tradingview-webhooks-bot is a python bot that works with tradingview's webhook alerts!
This bot is not affiliated with tradingview and was created by @robswc

You can follow development on github at: github.com/robswc/tradingview-webhook-bot

I'll include as much documentation here and on the repo's wiki!  I
expect to update this as much as possible to add features as they become available!
Until then, if you run into any bugs let me know!
"""

from actions import parse_webhook
from bitmexAPI import BitmexClient
from auth import get_token
from flask import Flask, request, abort


# Create Flask object called app.
app = Flask(__name__)
client = BitmexClient(api_key='1MkQqcpmTQFsPSX-uRL4OtTq',
                      api_secret='UOMrqg1s0P2XQCAVFRA80oPMpePp6QI27zGvKcEm2ifjb3LE',
                      test=True)


# Create root to easily let us know its on/working.
@app.route('/')
def root():
    return 'online'


@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        # Parse the string data from tradingview into a python dict
        data = parse_webhook(request.get_data(as_text=True))

        # Check that the key is correct
        if get_token() == data['token']:
            print(' [Alert Received] ')
            print('POST Received:', data)
            
            if data['action'] == 'long' or data['action'] == 'short close':
                res = client.place_order('buy', 'XBTUSD', 2)
                return res[0].__str__(), 200
            if data['action'] == 'short' or data['action'] == 'long close':
                res = client.place_order('sell', 'XBTUSD', 2)
                return res[0].__str__(), 200

        else:
            abort(403)
    else:
        abort(400)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)