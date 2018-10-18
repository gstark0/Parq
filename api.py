from flask import Flask, jsonify, render_template, request

import tensorflow as tf
import model as clf
import cctv as cctv

app = Flask(__name__)

# Get each spot's status with its exact position on the parking table
@app.route('/get_table', methods=['GET'])
def get_table():
	x = float(request.args.get('x'))
	y = float(request.args.get('y'))
	return jsonify(cctv.get_table([x, y]))

# Refresh info about all parking spots and update database
@app.route('/update')
def update():
	cctv.update()
	return 'updated'

# Train the TensorFlow model
@app.route('/train')
def train():
	clf.train()
	return 'trained'

@app.route('/')
def index():
	addr = cctv.get_addr()
	data = cctv.get_data()
	return render_template('index.html', data=[data, addr])

if __name__ == '__main__':
	app.run(debug=False)