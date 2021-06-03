import tensorflow as tf
import matplotlib.image as mpimg
import numpy as np


model = tf.keras.models.load_model("model")

print(model)

image = mpimg.imread("壓_18.jpeg")

image = np.array([image])

print(image.shape)

result = model.predict(image)
print(np.argmax(result))


