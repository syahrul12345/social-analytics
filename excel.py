import os
import xlsxwriter as xlsx
import json
import price
def run():
	subreddits = next(os.walk('./data'))[1]
	workbook = xlsx.Workbook("RedditAnalytics.xlsx")
	for subreddit in subreddits:
		if(subreddit == 'Antshares'):
			coin = 'Neo'
		elif(subreddit == 'Ethtrader'):
			coin = 'Ethereum'
		elif(subreddit == 'Cryptocurrency'):
			coin = 'Bitcoin'
			print(coin)
		else:
			coin = subreddit
		print("getting price for subreddit " + subreddit)
		print("getting prices for ....{}".format(coin))
		prices = price.run(coin.lower())
		worksheet = workbook.add_worksheet(subreddit)
		worksheet.write('A1','Subreddit data for {}'.format(subreddit))
		worksheet.write('A2','Date')
		worksheet.write('B2','Title')
		worksheet.write('C2','Score')
		worksheet.write('D2','Price')
		i = 3
		for file in os.listdir('./data/{}'.format(subreddit)):
			f = open('./data/{}/{}'.format(subreddit,file),"r")
			dataString = f.read()
			dataJSON = json.loads(dataString)
			importantData = dataJSON[subreddit]
			for data in importantData:
				worksheet.write('A{}'.format(i),data['date'])
				worksheet.write('B{}'.format(i),data['title'])
				worksheet.write('C{}'.format(i),data['score'])
				try:
					worksheet.write('D{}'.format(i),prices[data['date']])
				except:
					print("No date")
				i = i +1

	workbook.close()
run()