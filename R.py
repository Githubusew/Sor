from smartapi import SmartConnect
import pyotp
pyotp.TOTP(token).now()
 obj=SmartConnect(api_key=apikey)
 data = obj.generateSession(username,pwd,pyotp.TOTP(token).now())
 print(data)
 refreshToken= data['data']['refreshToken']
 res = obj.getProfile(refreshToken)
 print(res)
 from smartapi import SmartConnect
 from datetime import datetime
 import credentials
 import requests
 import numpy as np
try:
    orderparams = {
        "variety": "NORMAL",
        "tradingsymbol": "SBIN-EQ",
        "symboltoken": "3045",
        "transactiontype": "BUY",
        "exchange": "NSE",
        "ordertype": "LIMIT",
        "producttype": "INTRADAY",
        "duration": "DAY",
        "price": "19500",
        "squareoff": "0",
        "stoploss": "0",
        "quantity": "1"
        }
    orderId=obj.placeOrder(orderparams)
    print("The order id is: {}".format(orderId))
except Exception as e:
    print("Order placement failed:)
