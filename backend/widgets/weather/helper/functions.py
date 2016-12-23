import datetime as dt

def kelvinToCelsius(temp):
    return temp - 273.15

def timestampToDatetime(timestamp, format):
    return dt.datetime.fromtimestamp(
        int(timestamp)
    ).strftime(format)

def metersPerSecondToKilometersPerHour(ms):
    return ms*3.6

def meteorologyDegToWindDirection(deg):
    windDirection = ['N', 'NNE','NE','ENE','E','ESE','SE','SSE','S','SSW','SW','WSW','W','WNW','NW','NNW']
    index = round(deg/360*16);
    return windDirection[0 if index == 16 else index]
