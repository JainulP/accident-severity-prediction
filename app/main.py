from flask import Flask, render_template
from flask import request, redirect, make_response
from flask_cors import CORS
import os
import os.path
import json

app = Flask(__name__)
CORS(app)

@app.route("/")
def first_page():
    return render_template("index.html")
    
@app.route('/test', methods=['POST'])
def test():
     data = request.get_json()
     print("coming here")
     print(data)
     resp = make_response(json.dumps(data))
     resp.status_code = 200
     resp.headers['Access-Control-Allow-Origin'] = '*'
     return resp

# @app.route('/getPrediction', methods=['POST', 'GET'])
# def getPrediction():
# 	if request.method == 'POST':
# 		print("Reaching here")
# 	return render_template("index.html", result="Slight")

@app.route('/prediction', methods=['POST','GET'])
def prediction():
    if request.method == 'POST':
#         asd = request.json
        print("coming in post")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, threaded=True)