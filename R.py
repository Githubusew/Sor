token = 'DCASFPWTRVAJML7KW2QBWJ2DAY'

import pyotp

pyotp.TOTP(token).now()



from smartapi import SmartConnect
from smartapi.smartConnect import SmartConnect
import smartapi.smartExceptions



obj=SmartConnect(api_key = "KUiYK7su")     
data = obj.generateSession("a356453","Home~641",pyotp.TOTP(token).now())


refreshToken= data['data']['refreshToken']
feedToken=obj.getfeedToken()
userProfile= obj.getProfile(refreshToken)




try:
    orderparams = {
        "variety": "ROBO",
        "tradingsymbol": "SBIN-EQ",
        "symboltoken": "3045",
        "transactiontype": "SELL",
        "exchange": "NSE",
        "ordertype": "MARKET",
        "producttype": "BO",
        "duration": "DAY",
        "price": "195",
        "squareoff": "40",
        "stoploss": "20",
        "quantity": "1",
        "trailingStopLoss": "1"
        }
    orderId=obj.placeOrder(orderparams)
    print("The order id is: {}".format(orderId))
except Exception as e:
    print("Order placement failed: {}".format(e.message))
