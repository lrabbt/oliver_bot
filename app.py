from flask import Flask, jsonify, request
import json
from waitress import serve

app = Flask(__name__)

@app.route('/notifications', methods=['POST'])
def receive_notifications():
    content = request.get_json()
     
    with open('json_data.json', 'w') as f: 
     json.dump(content, f)

    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

@app.route('/')
def hello():
    return 'Hello, World'

if __name__ == "__main__":
   #app.run() ##Replaced with below code to run it using waitress
   serve(app, host='0.0.0.0', port=8000)
