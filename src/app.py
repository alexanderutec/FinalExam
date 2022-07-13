# Import dependencies
from cairo import Status
from flask import Flask, request
from httplib2 import Response, jsonify
from flask_wtf.csrf import CSRFProtect
import json
# Set global app
app = Flask(__name__)

# Set security flask
csrf = CSRFProtect()
csrf.init_app(app)
temp_info = {}

@app.route("/message/<str:topic>", methods=["GET"])
def get_message(topic):
    if topic not in temp_info:
        return Response(status=400,message="fail")
    return Response(jsonify(temp_info[topic]), 200)

@app.route("/message", methods=["POST"])
def post_message():
    if request.data:
        data = json.loads(request.data)
        message = data.get("message")
        topic = data.get("topic")
        if topic not in temp_info:
            temp_info[topic] = [message]
        else:
            temp_info[topic].append(message)
        return Response(status=200, message="ok")
    return Response(status=400, message="fail")