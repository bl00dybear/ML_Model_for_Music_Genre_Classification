import os
import subprocess
import yt_dlp as youtube_dl

def download_youtube_audio_as_wav(youtube_url, output_dir='test'):
    # Asigură-te că directorul de ieșire există
    os.makedirs(output_dir, exist_ok=True)

    try:
        # Setările yt-dlp pentru descărcarea audio
        ydl_opts = {
            'format': 'bestaudio/best',  # Selectează cel mai bun audio
            'outtmpl': os.path.join(output_dir, '%(id)s.%(ext)s'),  # Salvează fișierul în directorul specificat
            'quiet': True  # Ascunde informațiile de descărcare
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(youtube_url, download=True)
            filename = ydl.prepare_filename(info_dict)
            return filename
    except Exception as e:
        print(f"Eroare: {e}")
        return None

def convert_webm_to_wav_in_directory(dirr):
    for root, _, files in os.walk(dirr):
        for file in files:
            if file.endswith(".webm"):
                input_file = os.path.join(root, file)
                output_file = os.path.splitext(input_file)[0] + ".wav"

                # Obține durata fișierului folosind ffprobe
                ffprobe_command = f'ffprobe -i "{input_file}" -show_entries format=duration -v quiet -of csv="p=0"'
                result = subprocess.run(ffprobe_command, shell=True, capture_output=True, text=True)
                duration = float(result.stdout.strip())

                # Calculează punctul de start pentru segmentul de 30 de secunde
                start_time = max(0, (duration / 2) - 15)  # Evită valori negative

                # Comanda FFmpeg pentru conversie
                command = f'ffmpeg -loglevel quiet -ss {start_time} -t 30 -i "{input_file}" -ab 192k -ac 2 "{output_file}"'
                subprocess.call(command, shell=True)

                # Șterge fișierul .webm după conversie
                os.remove(input_file)
