import os
import librosa
import numpy as np


def extract_mfcc(file_path):
    try:
        y, sr = librosa.load(file_path, sr=None)
        # y stocheaza datele audio ca numere reprezentand un sample la un anumit moment
        # sr sample ratio (nr lor pe secunda)

        mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
        # Ia semnalul audio original y
        # Calculează transformarea Fourier a semnalului
        # Mapează rezultatul pe o scală de frecvență Mel, care imită mai bine percepția umană
        # Aplică o transformare cosinus discretă pentru a obține coeficienții MFCC
        # Returnează o matrice cu 13 rânduri (fiecare rând reprezintă un coeficient MFCC) și un număr de coloane egal cu numărul de cadre de timp din semnalul audio.

        return np.mean(mfccs.T, axis=0)

    except Exception as e:
        print(f"Eroare la procesarea fișierului {file_path}: {e}")
        return None

def read_data_folder():
    dataset_path = "../dataset"

    genres = os.listdir(dataset_path)

    data = {
        "mfcc": [],     # matricea procesata mai sus
        "labels": []    # genul melodiei
    }

    for genre in genres:
        genre_path = os.path.join(dataset_path, genre) #construim path ul genurilor
        if os.path.isdir(genre_path):
            for file in os.listdir(genre_path):
                file_path = os.path.join(genre_path, file)
                if file.endswith(".wav"):
                    mfcc = extract_mfcc(file_path)
                    if mfcc is not None:
                        data["mfcc"].append(mfcc)
                        data["labels"].append(genre)


