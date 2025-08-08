import os
import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/player/<player_tag>')
def get_player(player_tag):
    API_TOKEN = os.getenv("CLASH_API_TOKEN")
    if not API_TOKEN:
        return jsonify({"error": "API Token nicht gefunden! Bitte setze die Environment Variable CLASH_API_TOKEN."}), 500

    # Entferne führendes # aus player_tag, falls vorhanden
    player_tag = player_tag.lstrip('#')

    url = f"https://api.clashroyale.com/v1/players/%23{player_tag}"  # URL encodiere # als %23

    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return jsonify({
            "Name": data.get('name'),
            "Level": data.get('expLevel'),
            "Trophäen": data.get('trophies'),
            "Beste Trophäen": data.get('bestTrophies')
        })
    else:
        return jsonify({
            "error": f"API Fehler: {response.status_code}",
            "message": response.text
        }), response.status_code

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
