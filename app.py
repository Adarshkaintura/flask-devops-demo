from flask import Flask, request, jsonify
import os
import socket

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask DevOps Demo App!"

@app.route('/info')
def info():
    return jsonify({
        "app": "Flask DevOps Demo",
        "environment": os.getenv("APP_ENV", "development"),
        "host": socket.gethostname()
    })

@app.route('/api/square')
def square():
    try:
        num = int(request.args.get('num', 0))
        return jsonify({
            "input": num,
            "square": num ** 2
        })
    except ValueError:
        return jsonify({"error": "Invalid input"}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
