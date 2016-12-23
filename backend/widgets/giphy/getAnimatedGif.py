"""Importing JSON, Requests and urllib."""
import json
import requests
import urllib

tag = 'cute cats'
apiKey = 'dc6zaTOxFJmzC'
apiUrl = 'http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&{}'.format(urllib.parse.urlencode({'tag' : tag}))

def returnRandomGif():
    """Return random animated gif by tag."""
    r = requests.get(apiUrl)
    APIResponse = json.loads(r.text)

    return json.dumps(APIResponse['data']['image_original_url'], sort_keys=True)
