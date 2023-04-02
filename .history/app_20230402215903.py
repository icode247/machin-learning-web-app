from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import numpy as np
 
 # Load the saved model
model = tf.keras.models.load_model('linear_regression_model')
app = Flask(__name__)