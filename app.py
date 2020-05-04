from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/notifications', methods=['POST'])
def receive_notifications():
    content = request.get_json()
     
    with open('json_data.json', 'w') as f: 
     json.dump(content, f)

    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

@app.route('/hello')
def hello():
    return 'Hello, World'

