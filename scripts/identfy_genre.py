import os
import librosa
import numpy as np
import pandas as pd


def extract_mfcc(file_path, n_mfcc=128, n_fft=2048, hop_length=512):
    y, sr = librosa.load(file_path, sr=None)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc, n_fft=n_fft, hop_length=hop_length)
    mfccs = np.mean(mfccs.T, axis=0)

    return mfccs


def predict_genre(file_path, model, genres):
    mfccs = extract_mfcc(file_path)
    # print(mfccs)
    mfccs = mfccs.reshape(1,-1)# (1, 128)
    # print(mfccs.shape)
    prediction = model.predict(mfccs)
    predicted_genre = genres[np.argmax(prediction)]

    return predicted_genre

def predict_genre_from_first_file_in_directory(directory, model, genres):
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)

        if file.endswith('.wav'):
            predicted_genre = predict_genre(file_path, model, genres)
            print(f"Predicția pentru fișierul {file}: {predicted_genre}")
            return predicted_genre

    return None