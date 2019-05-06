import requests
from datetime import datetime
import json
def run(coin):
	priceDict = {}
	currency = coin
	url = "https://api.coingecko.com/api/v3/coins/{}/market_chart?vs_currency=usd&days=1500".format(coin)
	r = requests.get(url)
	try:
		priceData = r.json()['prices']
		for price in priceData:
			date = datetime.fromtimestamp(price[0]/1000).strftime('%d-%m-%Y')
			priceDict[date] = price[1]
		try:
			os.mkdir('./price/'.format(coin))
		except:
			print('')
		
		f=open('./price/{}.txt'.format(coin),"w+")
		f.write(str(priceDict))
		f.close()

		return priceDict
	except:
		return None
