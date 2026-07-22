import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image

# Load the model
model = tf.keras.models.load_model('keras_Model.h5')

# Load the label names
with open('labels.txt', 'r') as f:
    label_names = f.read().splitlines()

# Load and preprocess the image
img_path = 'dataset/test/acoustic neuroma/download (1).jpg'
img = image.load_img(img_path, target_size=(150, 150))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = x / 255.0

# Predict the class of the image
predictions = model.predict(x)
class_index = np.argmax(predictions[0])
class_name_predicted = label_names[class_index]

# Print the predicted class
print('Predicted class:', class_name_predicted)