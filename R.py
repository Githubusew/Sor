token = input("token")

import pyotp

pyotp.TOTP(token).now()



from smartapi import SmartConnect
from smartapi.smartConnect import SmartConnect
import smartapi.smartExceptions



obj=SmartConnect(api_key = input("api key"))     
data = obj.generateSession(input("id"), input("pwd") ,pyotp.TOTP(token).now())


refreshToken= data['data']['refreshToken']
feedToken=obj.getfeedToken()
userProfile= obj.getProfile(refreshToken)




try:
    orderparams = {
        "variety": "ROBO",
        "tradingsymbol": "BANKNIFTY",
        "symboltoken": input("symboltoken"),
        "transactiontype": "SELL",
        "exchange": "NFO",
        "ordertype": "MARKET",
        "producttype": "BO",
        "duration": "DAY",
        "price": "MARKET",
        "squareoff": "90",
        "stoploss": "5",
        "quantity": "1",
        "trailingStopLoss": "1"
        }
    orderId=obj.placeOrder(orderparams)
    print("The order id is: {}".format(orderId))
except Exception as e:
    print("Order placement failed: {}".format(e.message))
