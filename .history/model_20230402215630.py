# Load the dataset
import tensorflow as tf
import numpy as np
import pandas as pd

data = pd.read_csv('./housing_data.csv')


train_data = data.sample(frac=0.8, random_state=42)
test_data = data.drop(train_data.index)

model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1])
])
 
# Compile the model
model.compile(optimizer=tf.keras.optimizers.Adam(0.1), loss='mean_squared_error')

# Train the model
history = model.fit(train_data['Size'], train_data['Price'], epochs=100, verbose=False)


3
# Evaluate the model
loss = model.evaluate(test_data['Size'], test_data['Price'], verbose=False)
print(f"Mean squared error: {loss:.2f}")