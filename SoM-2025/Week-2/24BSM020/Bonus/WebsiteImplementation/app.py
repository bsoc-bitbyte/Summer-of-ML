from flask import Flask, render_template, request, jsonify
import json
import math
import os

app = Flask(__name__)

# Load data from JSON
with open('final_cccf.json', encoding='utf-8') as f:
    data = json.load(f)

# Prepare data lists
codechef = [row['codechef'] for row in data]
codeforces = [row['codeforces'] for row in data]

def linear_regression(X, y):
    n = len(X)
    mean_x = sum(X) / n
    mean_y = sum(y) / n
    numer = sum((X[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    denom = sum((X[i] - mean_x) ** 2 for i in range(n))
    slope = numer / denom if denom != 0 else 0
    intercept = mean_y - slope * mean_x
    return slope, intercept

def predict(x, slope, intercept):
    return slope * x + intercept

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_rating():
    data = request.json
    platform = data.get('platform')
    rating = float(data.get('rating'))
    if platform == 'codechef':
        X, y = codechef, codeforces
    elif platform == 'codeforces':
        X, y = codeforces, codechef
    else:
        return jsonify({'error': 'Invalid platform'}), 400
    slope, intercept = linear_regression(X, y)
    predicted = predict(rating, slope, intercept)
    return jsonify({'predicted_rating': round(predicted)})

if __name__ == '__main__':
    app.run(debug=True)