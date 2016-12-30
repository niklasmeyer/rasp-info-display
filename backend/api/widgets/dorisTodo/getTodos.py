"""Importing JSON, Requests and urllib."""
import json
import requests
import urllib


def getAPIKey():
    payload = {
        'user':'zookee1',
        'pass':'1'
    }
    apiUrl = "http://beta.dorisapp.com/api/1_0/auth/get_key.json"
    r = requests.get(apiUrl, auth=(payload['user'], payload['pass']))
    APIResponse = json.loads(r.text)
    return APIResponse['DRS_Success']['message']


def getTodaysToDos():
    apiKey = getAPIKey()
    apiUrl = "http://beta.dorisapp.com/api/1_0/tasks/view_all.json?{}".format(urllib.parse.urlencode({'apikey' : apiKey}))
    r = requests.get(apiUrl)
    APIResponse = json.loads(r.text)
    return APIResponse[0]['todos']
