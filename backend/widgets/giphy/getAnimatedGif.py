import requests
import json
import urllib

tag = 'cute cats'
apiKey = 'dc6zaTOxFJmzC'
apiUrl = 'http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&{}'.format(urllib.parse.urlencode({'tag' : tag}))

def returnRandomGif():
    r = requests.get(apiUrl)
    APIResponse = json.loads(r.text)

    return APIResponse['data']['image_original_url']
