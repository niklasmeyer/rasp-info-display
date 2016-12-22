import requests
import json
from backend.weather.helper.functions import kelvinToCelsius, timestampToDatetime, meteorologyDegToWindDirection, metersPerSecondToKilometersPerHour

cityId = 2944388  # bremen, germany
apiKey = '2cc05d69d27887219e0bda4640ef59ac'
apiUrl = 'http://api.openweathermap.org/data/2.5/weather?id=' + str(cityId) + '&APPID=' + apiKey

def returnWeatherConditions():

    r = requests.get(apiUrl)

    APIResponse = json.loads(r.text)

    temperature = kelvinToCelsius(APIResponse['main']['temp'])
    sunrise = timestampToDatetime(APIResponse['sys']['sunrise'], '%H:%M')
    sunset = timestampToDatetime(APIResponse['sys']['sunset'], '%H:%M')
    weatherConditions = APIResponse['weather'][0]['main']
    pressure = APIResponse['main']['pressure']
    cloudyPercent = APIResponse['clouds']['all']
    wind = {}
    wind['direction'] = meteorologyDegToWindDirection(APIResponse['wind']['deg'])
    wind['speed'] = metersPerSecondToKilometersPerHour(APIResponse['wind']['speed'])
    humidity = APIResponse['main']['humidity']


    response = {}
    response['main'] = {}
    response['main']['tempreature'] = temperature
    response['main']['conditions'] = weatherConditions
    response['main']['cloudyPercent'] = cloudyPercent
    response['main']['pressure'] = pressure
    response['main']['humidity'] = humidity
    response['daylight'] = {}
    response['daylight']['sunset'] = sunset
    response['daylight']['sunrise'] = sunrise
    response['wind'] = {}
    response['wind']['direction'] = wind['direction']
    response['wind']['speed'] = wind['speed']

    return response