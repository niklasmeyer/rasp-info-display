from flask import Flask
from flask_restful import Resource, Api
from backend.api.widgets.BSAG import getDepartures as bsag
from backend.api.widgets.giphy import getAnimatedGif as giphy
from backend.api.widgets.weather import getCurrentWeather as weather

app = Flask(__name__)
api = Api(app)

class BSAG(Resource):
    def get(self):
        return bsag.getDepartures()

class Giphy(Resource):
    def get(self):
        return giphy.returnRandomGif()

class Weather(Resource):
    def get(self):
        return weather.returnWeatherConditions()

api.add_resource(BSAG, '/bsag')
api.add_resource(Giphy, '/randomgif')
api.add_resource(Weather, '/weather')

if __name__ == '__main__':
    app.run(debug=True)