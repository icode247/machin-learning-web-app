# Load the dataset
import tensorflow as tf
import numpy as np
import pandas as pd

data = pd.read_csv('housing_data.csv')




htmlCopy code<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>House Price Predictor</title></head><body><h1>House Price Predictor</h1><form action="/predict" method="post"><label for="size">Size (in square feet):</label><input type="number" id="size" name="size" required><button type="submit">Predict Price</button></form></body></html>