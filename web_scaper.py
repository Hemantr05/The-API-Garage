from flask import Flask, jsonify, Response
from flask_cors import CORS

import requests
import logging
import flask
import json
import pandas as pd 
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
CORS(app)



def get_data(url, tag, id="seven-day-forecast", class_="tombstone-container"):
    """
        Args:
            url (str): URL or Link to the site to be scrapped
            tag (str): HTML tag to be extracted
            id (str): HTML id
            class_ (str): HTML class
        
        Returns:
            weather (dataframe): Returns dataframe
    """ 
    content, tag_content, id_content, class_content = None, None, None, None
    page = requests.get(url)
    if page.status_code == 200:
        content = BeautifulSoup(page.content, 'html.parser')
        if tag is not None:
            tag_content = content.find_all(tag)
        if id is not None:
            id_content = content.find(id=id)
        if class_ is not None:
            class_content = id_content.find_all(class_= class_)

        period_tags = id_content.select(".tombstone-container .period-name")
        periods = [pt.get_text() for pt in period_tags]
        short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
        temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
        descs = [d["title"] for d in seven_day.select(".tombstone-container img")]
        # print(short_descs)
        # print(temps)
        # print(descs)

    weather = pd.DataFrame({
        "period": periods,
        "short_desc": short_descs,
        "temp": temps,
        "desc":descs
    })
    


@app.route('/', methods=["GET", "POST"])
def return_data():
    if request.method == "GET":
        return "OK"

    if request.method == "POST":
        try:
            url = flask.request.form.get("url", "https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
            tag = flask.request.form.get("tag", None)
            id_ = flask.request.form.get("id", "seven-day-forecast"")
            class_ = flask.request.form.get("class", "tombstone-container")
            data = get_data(url, tag, id_, class_)

            data = data.to_json(orient="records"), mimetype='application/json')

            return Response(response=json.dumps(data),
									status=200,
									mimetype="application/json")
        except:
			return Response(response=json.dumps({"error":"An Error Occurred"}), status=404, mimetype="application/json")
    else:
		return Response(response=json.dumps({"error":"Query or workorder_json Empty"}), status=404, mimetype="application/json")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8082)))