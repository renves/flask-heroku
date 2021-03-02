from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)

@app.route('/')
def get():
	return jsonify({"message": "ok"})

if __name__ == '__main__':
    app.run(threaded=True, port=8080)
