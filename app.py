from flask import Flask
from flask_cors import CORS
import requests
import json


app = Flask(__name__)
CORS(app)

@app.route("/fetch-candidates")
def get_response():
  response = requests.get("https://hs-resume-data.herokuapp.com/v3/candidates/all_data_b1f6-acde48001122")
  data = {"data": response.json()}
  return data


if __name__ == "__main__":
    app.run()