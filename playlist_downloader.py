import os
import subprocess
from pytube import Playlist
from scripts.process_youtube_song import convert_webm_to_wav_in_directory


def convert_webm_to_wav_in_directory2(dirr):
    for root, _, files in os.walk(dirr):
        for file in files:
            if file.endswith(".ogg"):
                input_file = os.path.join(root, file)
                base_output_name = os.path.splitext(input_file)[0]

                # Obține durata fișierului folosind ffprobe
                ffprobe_command = f'ffprobe -i "{input_file}" -show_entries format=duration -v quiet -of csv="p=0"'
                result = subprocess.run(ffprobe_command, shell=True, capture_output=True, text=True)
                try:
                    duration = float(result.stdout.strip())
                except ValueError:
                    print(f"Nu s-a putut obține durata pentru fișierul {input_file}")
                    continue

                # Începe extragerea segmentelor
                start_time = 60  # Începe de la 1:00 (60 secunde)
                max_intervals = 5
                intervals_extracted = 0
                pause_between_intervals = 10
                segment_duration = 30
                min_remaining_time = 45  # Evită ultimele 45 de secunde

                while start_time + segment_duration < duration - min_remaining_time and intervals_extracted < max_intervals:
                    output_file = f"{base_output_name}_segment_{intervals_extracted + 1}.wav"

                    # Comanda FFmpeg pentru conversie
                    command = f'ffmpeg -loglevel quiet -ss {start_time} -t {segment_duration} -i "{input_file}" -ab 192k -ac 2 "{output_file}"'
                    subprocess.call(command, shell=True)

                    print(f"Generat: {output_file}")

                    # Trecem la următorul segment
                    start_time += segment_duration + pause_between_intervals
                    intervals_extracted += 1

                # Șterge fișierul .webm după conversie
                os.remove(input_file)
                print(f"Șters fișierul original: {input_file}")

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


    convert_webm_to_wav_in_directory2(output_directory)

    print(f"Toate fișierele au fost procesate și salvate în {output_directory}")


if __name__ == "__main__":
    main()
