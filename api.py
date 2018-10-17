from flask import Flask, jsonify, render_template, request

import tensorflow as tf
import model as clf
import cctv as cctv

app = Flask(__name__)

# Return parking info from database
@app.route('/get_data')
def get_data():
	return jsonify(cctv.get_data())

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
	return render_template('index.html')

if __name__ == '__main__':
	app.run()