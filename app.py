from flask import Flask
from flask import request, jsonify, make_response, render_template
import random

app = Flask(__name__, template_folder='.')

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/weather/get_by_location", methods=["POST"])
def get_by_location():

    req = request.get_json()

    print(req)

    # Do your logic here

    city = random.choice(['London', 'New York', 'Rome'])
    temperature = random.choice(range(2,30))


    res = make_response(jsonify({"message": "OK",
    	                         "city": city,
    	                         "temperature": temperature }), 200)

    return res
