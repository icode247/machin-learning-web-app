# Load the dataset
import tensorflow as tf
import numpy as np
import pandas as pd

data = pd.read_csv('housing_data.csv')




@app.route('/predict', methods=['POST'])
def predict():
      size = float(request.form['size'])
      price = model.predict(np.array([size]))[0][0]
      return jsonify({'price': price})