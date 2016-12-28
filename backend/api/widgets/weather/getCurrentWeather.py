"""Importing JSON, Requests and defaultdict."""
import json
import requests
from collections import defaultdict
from backend.api.widgets.weather.helper.functions import kelvinToCelsius, timestampToDatetime, meteorologyDegToWindDirection, \
        metersPerSecondToKilometersPerHour

def returnWeatherConditions():
    """Return JSON of the current weather, which was gathered off of the openwaeatherAPI."""
    cityId = 2944388  # bremen, germany
    apiKey = '2cc05d69d27887219e0bda4640ef59ac'
    apiUrl = 'http://api.openweathermap.org/data/2.5/weather?id={}&APPID={}'.format(str(cityId),apiKey)

    r = requests.get(apiUrl)
    APIResponse = json.loads(r.text)

    response = defaultdict(dict)
    response['main']['tempreature'] = kelvinToCelsius(APIResponse['main']['temp'])
    response['main']['conditions'] = APIResponse['weather'][0]['main']
    response['main']['cloudyPercent'] = APIResponse['clouds']['all']
    response['main']['pressure'] = APIResponse['main']['pressure']
    response['main']['humidity'] = APIResponse['main']['humidity']
    response['daylight']['sunrise'] = timestampToDatetime(APIResponse['sys']['sunrise'], '%H:%M')
    response['daylight']['sunset'] = timestampToDatetime(APIResponse['sys']['sunset'], '%H:%M')
    response['wind']['direction'] = meteorologyDegToWindDirection(APIResponse['wind']['deg'])
    response['wind']['speed'] = metersPerSecondToKilometersPerHour(APIResponse['wind']['speed'])

    return json.dumps(response, sort_keys=True)
