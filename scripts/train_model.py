import pandas as pd
import numpy as np
import tensorflow as tf
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder



def construct_model(path_dataset_csv,dataset_path):
    data_frame = pd.read_csv(path_dataset_csv)

    x = np.array([np.fromstring(f, sep=' ') for f in data_frame["mfcc"]])
    y = data_frame["label"]

    encoder = LabelEncoder()
    y_encoded = encoder.fit_transform(y)

    #impartirea datasetului in training si test

    x_train, x_test, y_train, y_test = train_test_split(x, y_encoded, test_size=0.2, random_state=42)

    genres = os.listdir(dataset_path)

    model = tf.keras.Sequential([
        tf.keras.layers.Dense(128, input_shape=(x_train.shape[1],), activation='relu'),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keres.layers.Dense(len(genres), activation='softmax')
    ])

    model.compile(optimizer='adam',loss='sparse_categorical_cross entropy',metrics=['accuracy'])
