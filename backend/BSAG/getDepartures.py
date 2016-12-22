import requests
import datetime as dt
from xml.dom import minidom
import time


timestamp = time.time()
departures = []
walkingTime = 7

stationId = '000691055'
#get station id here: http://fahrplaner.vbn.de/hafas/ajax-getstop.exe/dny?start=1&REQ0JourneyStopsS0A=1&REQ0JourneyStopsB=12&S=##################################&js=true -> extId
dirs = {"Kirchbachstr./4S Lilienthal", "Borgfeld", "Kattenturm/Klinikum LDW"}
bsag_url = "http://fahrplaner.vbn.de/bin/stboard.exe/dn"
payload = {
    'productsFilter': '11111111111111',
    'boardType': 'dep',
    'L': 'vs_java3',
    'date': dt.datetime.fromtimestamp(int(timestamp)).strftime('%d.%m.%Y'),
    'time': dt.datetime.fromtimestamp(int(timestamp)).strftime('%H:%S'),
    'maxJourneys': '50',
    'start': 'yes',
    'inputTripelId': 'L=' + str(stationId)
}

def getDepartures():
    r = requests.post(bsag_url, data=payload)
    APIResponse = r.text

    xmldoc = minidom.parseString(APIResponse)
    itemlist = xmldoc.getElementsByTagName('Journey')

    for journey in itemlist:
        if journey.attributes['dir'].value in dirs:
            departures.append({
                'departureTime':journey.attributes['fpTime'].value,
                'line':journey.attributes['hafasname'].value,
                'destination':journey.attributes['targetLoc'].value,
                'delay':journey.attributes['delay'].value,
                'walkingTime': walkingTime
            })


    return departures


print(getDepartures())