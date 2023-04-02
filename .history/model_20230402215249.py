# Load the dataset
import tensorflow as tf
import numpy as np
import pandas as pd

data = pd.read_csv('./housing_data.csv')


train_data = data.sample(frac=0.8, random_state=42)
test_data = data.drop(train_data.index)

print(f"{train_data}")