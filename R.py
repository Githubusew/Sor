from smartapi import SmartConnect
import pyotp
token = ' DCASFPWTRVAJML7KW2QBWJ2DAY '
import pyotp
pyotp.TOTP(token).now()
apikey = ' KUiYK7su '
username = ' a356453 '
pwd = ' Home~641 '
token = ' DCASFPWTRVAJML7KW2QBWJ2DAY '
obj=SmartConnect(api_key=apikey)
data = obj.generateSession(username,pwd,pyotp.TOTP(token).now())
print(data)
