import os
import librosa
import numpy as np
import pandas as pd


def extract_mfcc(file_path, n_mfcc=128, n_fft=2048, hop_length=512):
    # Încarcă fișierul audio
    signal, sr = librosa.load(file_path, sr=None)  # sr=None păstrează rata de eșantionare originală

    # Extrage MFCC folosind argumente cheie
    mfccs = librosa.feature.mfcc(y=signal, sr=sr, n_mfcc=n_mfcc, n_fft=n_fft, hop_length=hop_length)

    # Poți normaliza MFCC-urile sau le poți reda direct
    mfccs = np.mean(mfccs, axis=1)  # Poți calcula media pe întreaga durată a semnalului

    return mfccs


def predict_genre(file_path, model, genres):
    # Extrage coeficientii MFCC si redimensioneaza pentru a fi compatibili cu modelul
    mfccs = extract_mfcc(file_path)
    print(mfccs)
    mfccs = mfccs.reshape(1,13)# (1, 128)
    print(mfccs)
    prediction = model.predict(mfccs)
    predicted_genre = genres[np.argmax(prediction)]  # Returnează genul cu probabilitatea maximă
    # print("aiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiixi")


    return predicted_genre

def predict_genre_from_first_file_in_directory(directory, model, genres):
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)

        if file.endswith('.wav'):
            predicted_genre = predict_genre(file_path, model, genres)
            print(f"Predicția pentru fișierul {file}: {predicted_genre}")
            return predicted_genre

    return None