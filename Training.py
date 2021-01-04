import pathlib
import tensorflow as tf
import numpy as np
from tensorflow.keras import layers

# presetting

data_dir = pathlib.Path("./dataset")
batchSize = 16
imageHeight = 250
imageWidth = 250

def loadDataset():
    train = tf.keras.preprocessing.image_dataset_from_directory(
        data_dir,
        validation_split=0.2,
        subset="training",
        seed=123,
        image_size=(imageHeight, imageWidth),
        batch_size=batchSize)

    val = tf.keras.preprocessing.image_dataset_from_directory(
        data_dir,
        validation_split=0.2,
        subset="validation",
        seed=123,
        image_size=(imageHeight, imageWidth),
        batch_size=batchSize)

    normalization_layer = tf.keras.layers.experimental.preprocessing.Rescaling(1. / 255)

    normalized_ds = train.map(lambda x, y: (normalization_layer(x), y))
    normalized_valds = val.map(lambda x, y: (normalization_layer(x), y))
    #normalized_ds = normalized_ds.cache().prefetch(buffer_size=tf.data.experimental.AUTOTUNE)
    #normalized_valds = normalized_valds.cache().prefetch(buffer_size=tf.data.experimental.AUTOTUNE)

    return normalized_ds, normalized_valds



def getModel():
    model = tf.keras.Sequential([
        layers.Conv2D(64, 3, activation='relu'),
        layers.MaxPooling2D(),
        layers.Conv2D(64, 3, activation='relu'),
        layers.MaxPooling2D(),
        layers.Conv2D(64, 3, activation='relu'),
        layers.MaxPooling2D(),
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(1500)
    ])

    model.compile(
        optimizer='adam',
        loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
        metrics=['accuracy'])

    return model


train_ds, val_ds = loadDataset()

model = getModel()
model.fit(
    train_ds,
    validation_data=train_ds,
    epochs=5
)

model.summary()