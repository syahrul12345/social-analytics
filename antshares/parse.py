import matplotlib.pyplot as plt
import ast
import requests
from datetime import datetime
import time
import matplotlib.dates as mdates
import matplotlib.cbook as cbook
import matplotlib.dates as mdates

dateAxis  = []
subscriberAxis = []
dateAxis2 = []
priceAxis = []
	
def getSubscriber(subreddit):
	url = "http://redditmetrics.com/ajax/compare.reddits"
	formData = {'reddit0':subreddit,'reddit1':'_thread','reddit2':'','reddit3':'','reddit4':''}
	r = requests.post(url,data=formData)
	dataInfo = r.json()['message']['total']['data']
	for data in dataInfo:
		try:
			subscriberAxis.append(int(data['a']))
			unixDate = time.mktime(datetime.strptime(data['y'],'%Y-%m-%d').timetuple())
			dateAxis.append(datetime.fromtimestamp(unixDate))
		except:
			"Not an 'a' tag"
	
def price(coin):
	currency = coin
	url = "https://api.coingecko.com/api/v3/coins/{}/market_chart?vs_currency=usd&days=900".format(currency)
	r = requests.get(url)
	priceData = r.json()['prices']
	for price in priceData:
		dateAxis2.append(datetime.fromtimestamp(price[0]/1000))
		priceAxis.append((price[1]))
	# plt.plot(dateAxis2,priceAxis)
	# plt.show()

def plot():
	# years = mdates.YearLocator()   # every year
	months = mdates.MonthLocator()  # every month
	# yearsFmt = mdates.DateFormatter('%Y')

	fig, ax1 = plt.subplots()
	# ax1.xaxis.set_major_locator(months)
	# ax1.xaxis.set_major_formatter(yearsFmt)
	ax1.xaxis.set_minor_locator(months)
	ax1.format_xdata = mdates.DateFormatter('%Y-%m-%d')
	
	color = 'tab:red'
	ax1.set_xlabel('Date')
	ax1.set_ylabel('Reddit Subscriber Count', color=color)
	ax1.plot_date(mdates.date2num(dateAxis),subscriberAxis, color=color,fmt='-')
	ax1.tick_params(axis='y', labelcolor=color)

	ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
	color = 'tab:green'
	ax2.set_ylabel('Price(USD)', color=color)  # we already handled the x-label with ax1
	ax2.plot_date(mdates.date2num(dateAxis2), priceAxis, color=color,fmt='-')
	ax2.tick_params(axis='y', labelcolor=color)

	fig.tight_layout()  # otherwise the right y-label is slightly clipped
	fig.autofmt_xdate()

	plt.show()


getSubscriber("Antshares")
price("neo")
plot()
