import os
import subprocess
from pytube import Playlist
from scripts.process_youtube_song import convert_webm_to_wav_in_directory


def download_youtube_playlist(playlist_url, output_directory):
    # Comandă yt-dlp pentru descărcare audio în format webm
    command = f'yt-dlp -f bestaudio --extract-audio --audio-format vorbis --audio-quality 0 -o "{output_directory}/%(title)s.%(ext)s" {playlist_url}'
    subprocess.call(command, shell=True)

def main():
    youtube_playlist_url = input("Introduceți link-ul către playlist-ul YouTube: ")
    music_genre = input("Introduceți genul muzical: ").strip().lower()

    output_directory = f"/home/sebi/ML_Learning/ML_Model_for_Music_Genre_Classification/dataset/raw/{music_genre}"
    os.makedirs(output_directory, exist_ok=True)

    print("Descărcăm playlist-ul...")
    download_youtube_playlist(youtube_playlist_url, output_directory)

    print("Conversia fișierelor .webm în .wav...")
    convert_webm_to_wav_in_directory(output_directory)

    print(f"Toate fișierele au fost procesate și salvate în {output_directory}")


if __name__ == "__main__":
    main()
