# Load the dataset
import tensorflow as tf
import numpy as np
import pandas as pd

data = pd.read_csv('housing_data.csv')




@app.route('/')
def index():
    return render_template('index.html')