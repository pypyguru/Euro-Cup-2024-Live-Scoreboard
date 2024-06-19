from flask import *
import requests
import config

app = Flask(__name__)

@app.route("/")
def index():
    def get_standings():
            uri = 'https://api.football-data.org/v4/competitions/EC/standings'
            headers = { 'X-Auth-Token': config.API_TOKEN }
            response = requests.get(uri, headers=headers)
            standings = response.json()["standings"]
            return standings
    def get_matches():
            uri = 'https://api.football-data.org/v4/competitions/EC/matches'
            headers = { 'X-Auth-Token': config.API_TOKEN }
            response = requests.get(uri, headers=headers)
            matches = response.json()["matches"]
            return matches
    return render_template('index.html', standings=get_standings(), matches=get_matches())

if __name__ == '__main__':
    app.run(debug=True)
  