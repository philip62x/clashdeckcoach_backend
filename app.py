from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

API_TOKEN = "DEIN_API_TOKEN_HIER"

@app.route('/player/<player_tag>')
def get_player(player_tag):
    url = f"https://api.clashroyale.com/v1/players/{player_tag}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": f"API request failed with status {response.status_code}"}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
