import pathlib

import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

data_dir = pathlib.Path("./dataset")

for wordDir in data_dir.iterdir():
    plt.figure(figsize=(9, 9))
    i = 1

    if wordDir.is_dir():
        words = list(wordDir.glob("*"))
        for word in wordDir.iterdir():
            # plt.subplot(int(len(words) / 5), 5, i)
            # plt.imshow(image.imread(word))
            i += 1

batchSize = 8
imageHeight = 250
imageWidth = 250

imageGenerator = tf.keras.preprocessing.image.ImageDataGenerator(validation_split=0.2, )

train_ds = tf.keras.preprocessing.image.DirectoryIterator(
    directory=data_dir,
    image_data_generator=imageGenerator,
    color_mode="rgb",
    subset="training",
    seed=123,
    target_size=(imageHeight, imageWidth),
    batch_size=batchSize)

val_ds = tf.keras.preprocessing.image.DirectoryIterator(
    directory=data_dir,
    image_data_generator=imageGenerator,
    color_mode="grayscale",
    subset="validation",
    seed=123,
    target_size=(imageHeight, imageWidth),
    batch_size=batchSize)

print(train_ds)
class_names = train_ds.class_indices
print(class_names)

for image_batch, labels_batch in train_ds:
    print(image_batch.shape)
    print(labels_batch.shape)
    break

num_classes = 20

model = Sequential([
    layers.experimental.preprocessing.Rescaling(1. / 255, input_shape=(250, 250, 3)),
    layers.Conv2D(16, 3, padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(32, 3, padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(64, 3, padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(num_classes)
])

model.compile(optimizer='adam',
              loss=tf.keras.losses.CategoricalCrossentropy(),
              metrics=['accuracy'])

model.summary()

epochs = 10
history = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=epochs
)
