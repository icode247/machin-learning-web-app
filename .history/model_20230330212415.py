# Load the dataset
import tensorflow as tf
import numpy as np
import pandas as pd

data = pd.read_csv('housing_data.csv')




pythonCopy code# Load the saved modelmodel = tf.keras.models.load_model('linear_regression_model')