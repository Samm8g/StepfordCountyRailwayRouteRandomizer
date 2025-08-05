from flask import Flask, render_template, jsonify, request
import random
from stations import stations

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/randomize')
def randomize():
    difficulty = request.args.get('difficulty', default=3, type=int)
    startPoint = random.choice(stations)
    endPoint = random.choice(stations)
    while endPoint == startPoint:
        endPoint = random.choice(stations)
    return jsonify({'route': f'Starting station: {startPoint}\nEnding station: {endPoint}'})

if __name__ == '__main__':
    app.run(debug=True, port=5001)