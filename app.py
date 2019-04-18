import appToken as token
import requests
import requests.auth
import json
import pprint
pp = pprint.PrettyPrinter(indent=4)

global url;
url = "https://oauth.reddit.com"
def getToken():
	secret = token.secret()
	client = token.client()
	user = token.user()
	password = token.password()
	url = "https://www.reddit.com/api/v1/access_token";
	client_auth = requests.auth.HTTPBasicAuth(client,secret)
	headers = {"User-Agent": "Windows by Syahrul@Talenta"}
	payload = {'grant_type':'password','username':user,'password':password}
	r = requests.post(url,data=payload,auth=client_auth,headers=headers)
	return r.json()['access_token']

def getInfo(access_token):
	#get individual info of u/ZV_chain , this function has no use
	endPoint = "/api/v1/me"
	endUrl = url + endPoint
	headers = {'Authorization':'bearer {}'.format(access_token),"User-Agent": "Windows by Syahrul@Talenta"}
	return requests.get(url,headers=headers).json()

def about(access_token,subreddit):
	endPoint = "/r/{}/about.json".format(subreddit)
	url = "https://reddit.com"
	endUrl = url + endPoint
	print(endUrl)
	headers = {'Authorization':'bearer {}'.format(access_token),"User-Agent": "Windows by Syahrul@Talenta"}
	return requests.get(endUrl,headers=headers).json()



pp.pprint(about(getToken(),'Neo'))