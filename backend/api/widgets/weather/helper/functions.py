"""Importing dateime."""
import datetime as dt

def kelvinToCelsius(temp):
    """Return the temperature calculated from kelvin to celcius."""
    return temp - 273.15

def timestampToDatetime(timestamp, format):
    """Return Datetime by timestamp."""
    return dt.datetime.fromtimestamp(
        int(timestamp)
    ).strftime(format)

def metersPerSecondToKilometersPerHour(ms):
    """Return km/h by calculating off of m/s."""
    return ms*3.6

def meteorologyDegToWindDirection(deg):
    """Return the winddirection by meteorologyDegree."""
    windDirection = ['N', 'NNE','NE','ENE','E','ESE','SE','SSE','S','SSW','SW','WSW','W','WNW','NW','NNW']
    index = round(deg/360*16)
    return windDirection[0 if index == 16 else index]
