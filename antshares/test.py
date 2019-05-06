import matplotlib.pyplot as plt
import ast
import requests
import datetime
import time
dateAxis  = []
subscriberAxis = []
def getSubscriber(subreddit):
	url = "http://redditmetrics.com/ajax/compare.reddits"
	formData = {'reddit0':subreddit,'reddit1':'_thread','reddit2':'','reddit3':'','reddit4':''}
	r = requests.post(url,data=formData)
	dataInfo = r.json()['message']['total']['data']
	
	for data in dataInfo:
		print(data)
		try:
			subscriberAxis.append(int(data['a']))
			unixDate = time.mktime(datetime.datetime.strptime(data['y'],'%Y-%m-%d').timetuple())
			dateAxis.append(unixDate)
		except:
			"Not an 'a' tag"
	plt.plot(dateAxis,subscriberAxis)
	plt.show()
getSubscriber("Antshares")

