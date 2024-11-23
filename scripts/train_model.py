import pandas as pd
import numpy as np
import tensorflow as tf
import os

from keras.src.callbacks import EarlyStopping
from keras.src.utils.module_utils import tensorflow
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder




def construct_model(path_dataset_csv,dataset_path):
    data_frame = pd.read_csv(path_dataset_csv)

    model_directory = "/home/sebi/ML_Learning/ML_Model_for_Music_Genre_Classification/models"

    x = np.array([np.fromstring(f, sep=' ') for f in data_frame["mfcc"]])
    y = data_frame["labels"]

    encoder = LabelEncoder()
    y_encoded = encoder.fit_transform(y)

    #impartirea datasetului in training si test

    x_train, x_test, y_train, y_test = train_test_split(x, y_encoded, test_size=0.2, random_state=42)

    genres = os.listdir(dataset_path)

    model = tf.keras.Sequential([
        tf.keras.layers.Dense(128, input_shape=(x_train.shape[1],), activation='relu', kernel_regularizer=tensorflow.keras.regularizers.l2(0.01)),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Dropout(0.5),

        tf.keras.layers.Dense(64, activation='relu', kernel_regularizer=tensorflow.keras.regularizers.l2(0.01)),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Dropout(0.3),

        tf.keras.layers.Dense(32, activation='relu', kernel_regularizer=tensorflow.keras.regularizers.l2(0.01)),
        tf.keras.layers.Dropout(0.3),

        tf.keras.layers.Dense(len(genres), activation='softmax')
    ])

    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy'])

    early_stopping = EarlyStopping(
        monitor='val_loss',
        patience=3,  # Oprește dacă nu există îmbunătățiri în 3 epoci consecutive
        restore_best_weights=True
    )

    history = model.fit(
        x_train, y_train,
        epochs=100,
        batch_size=32,
        validation_data=(x_test, y_test),
        callbacks=[early_stopping]
    )

    loss, accuracy = model.evaluate(x_test, y_test)
    print(f'Loss: {loss}, Accuracy: {accuracy}')

    os.makedirs(model_directory, exist_ok=True)
    model.save(os.path.join(model_directory, 'music_genre_classifier.h5'))
    print(f'Model saved at {model_directory}')

    return history

