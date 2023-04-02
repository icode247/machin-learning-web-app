from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import numpy as np
 
 # Load the saved model
model = tf.keras.models.load_model('linear_regression_model')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    size = float(request.form['size'])
    price = model.predict(np.array([size]))[0][0]
    return jsonify({'price': price})