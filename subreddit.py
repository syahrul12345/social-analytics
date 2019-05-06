import appToken as token
import requests
import requests.auth
import json
import pprint
import praw
from datetime import datetime
import time
import xlsxwriter
import xlrd
import xlwt
import os

subredditDict={}
url = "https://api.pushshift.io/reddit/search/submission"
def getSubmission(subreddits,after,before,karma):
	unixAfter = int(time.mktime(datetime.strptime(after,'%d-%m-%Y').timetuple()))
	unixBefore = int(time.mktime(datetime.strptime(before,'%d-%m-%Y').timetuple()))
	currentTime = time.time()
	daysAfter = int((currentTime - unixAfter)/86400)
	daysBefore = int((currentTime - unixBefore)/86400)
	daysDiff = daysAfter - daysBefore
	for subreddit in subreddits:
		answer = []
		for i in range(daysBefore,daysAfter+1):
			print("Downloading data for {}....".format(subreddit))
			endPoint = "/?subreddit={}&after={}d&before={}d&sort=asc&size=500&filter=title,score,created_utc,permalink&aggs=link_id".format(subreddit,i+1,i)
			answer = getData(url+endPoint,50)
			#answer is a list of all entries for a subreddit in a 1 day period
			save(answer,subreddit)
		
def getData(url,karma):
	data = requests.get(url).json()
	submissions = data["data"]
	infoDict = []
	for submission in submissions:
		title = submission["title"]
		realDate = datetime.fromtimestamp(submission["created_utc"]).strftime("%d-%m-%Y")
		score = int(submission["score"])
		link = submission["permalink"]
		if(score >= karma):
			currentSubmission = {"title":title,"date":str(realDate),"score":score,"link":link}
			infoDict.append(currentSubmission)
	return infoDict

def save(answer,subreddit):
	dictToSave = {}
	dictToSave[subreddit] = answer
	#lets get teh first date
	try:
		os.mkdir('./data/{}'.format(subreddit))
	except:
		print('')
	try:
		firstDate = answer[0]['date']
		lastDate = answer[-1]['date']3
		subredditJSON = json.dumps(dictToSave)
		f = open("./data/{}/{} to {}.txt".format(subreddit,firstDate,lastDate),"w+")
		f.write(subredditJSON)
		f.close()
	except:
		print('')
	
		
#subreddits to scan
subreddits = ["Cryptocurrency"]
getSubmission(subreddits,"01-01-2017","02-05-2019",50)
