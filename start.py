import tensorflow
import os
import shutil
from main import *
from scripts.process_youtube_song import download_youtube_audio_as_wav
from scripts.process_youtube_song import convert_webm_to_wav_in_directory
from scripts.identfy_genre import predict_genre_from_first_file_in_directory

if __name__ == "__main__":
    output_dir = "test"
    directory = output_dir
    genres = ['hiphop', 'rock']
    model_path = '/home/sebi/ML_Learning/ML_Model_for_Music_Genre_Classification/models/music_genre_classifier.h5'
    source_folder = "/home/sebi/ML_Learning/ML_Model_for_Music_Genre_Classification/test"

    continui = 1
    rasp = 1

    while continui == 1:
        youtube_link = input("Introduceți link-ul YouTube: ")
        download_youtube_audio_as_wav(youtube_link, output_dir)
        convert_webm_to_wav_in_directory(directory)
        model = tensorflow.keras.models.load_model(model_path)
        print("ajunge aici")
        # print(model.summary())
        predict_genre_from_first_file_in_directory(directory, model, genres)

        print("It is correct? [0/1] ")
        rasp = int(input())
        # print(rasp)

        if rasp == 0:
            genre = input("Introduce genre:")
            destination_folder = f"/home/sebi/ML_Learning/ML_Model_for_Music_Genre_Classification/dataset/raw/{genre}"
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            # Parcurgem fișierele din folderul sursă
            for file in os.listdir(source_folder):
                if file.endswith(".wav"):  # Căutăm doar fișierele .wav
                    source_path = os.path.join(source_folder, file)
                    destination_path = os.path.join(destination_folder, file)

                    # Mutăm fișierul în folderul de destinație
                    shutil.move(source_path, destination_path)
            create_model()


        continui =int(input("Continue? [0/1] "))
        # print(continui)


# https://www.youtube.com/watch?v=dHUHxTiPFUU&ab_channel=Metallica