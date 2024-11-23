import tensorflow
from scripts.process_youtube_song import download_youtube_audio_as_wav
from scripts.process_youtube_song import convert_webm_to_wav_in_directory
from scripts.identfy_genre import predict_genre_from_first_file_in_directory

if __name__ == "__main__":
    youtube_link = input("Introduceți link-ul YouTube: ")
    output_dir = "test"
    download_youtube_audio_as_wav(youtube_link, output_dir)

    directory = output_dir
    convert_webm_to_wav_in_directory(directory)

    genres = ['blues', 'classical', 'country', 'disco', 'hiphop', 'metal', 'pop', 'reggae', 'rock']

    # Actualizează calea modelului
    model_path = '/home/sebi/ML_Learning/ML_Model_for_Music_Genre_Classification/models/music_genre_classifier.h5'
    model = tensorflow.keras.models.load_model(model_path)

    print(model.summary())

    predict_genre_from_first_file_in_directory(directory, model, genres)
