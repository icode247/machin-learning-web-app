# Load the dataset
import tensorflow as tf
import numpy as np
import pandas as pd

data = pd.read_csv('housing_data.csv')




from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import numpy as np

app = Flask(__name__)