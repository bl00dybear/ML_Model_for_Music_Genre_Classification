import os
import subprocess


def convert_ogg_to_wav_in_directory(directory):
    # Verifică dacă directorul introdus există
    if not os.path.isdir(directory):
        print(f"Directorul specificat nu există: {directory}")
        return

    print(f"Conversia fișierelor .ogg în .wav în directorul: {directory}")

    # Iterează prin toate fișierele din director
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".ogg"):
                input_file = os.path.join(root, file)
                output_file = os.path.splitext(input_file)[0] + ".wav"

                # Comanda FFmpeg pentru conversie
                command = f'ffmpeg -loglevel quiet -i "{input_file}" -acodec pcm_s16le -ar 44100 "{output_file}"'

                print(f"Converting: {input_file} -> {output_file}")
                subprocess.call(command, shell=True)

                # Opțional: șterge fișierul .ogg original după conversie
                # os.remove(input_file)

    print("Conversia tuturor fișierelor .ogg a fost finalizată.")


def delete_ogg_files_in_directory(directory):
    # Verifică dacă directorul introdus există
    if not os.path.isdir(directory):
        print(f"Directorul specificat nu există: {directory}")
        return

    print(f"Ștergerea fișierelor .ogg din directorul: {directory}")

    # Iterează prin toate fișierele din director
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".ogg"):
                file_path = os.path.join(root, file)
                os.remove(file_path)  # Șterge fișierul
                print(f"Șters: {file_path}")

    print("Toate fișierele .ogg au fost șterse.")


def main():
    # Cere utilizatorului directorul unde se află fișierele
    directory = input("Introduceți calea către directorul cu fișiere .ogg: ").strip()
    convert_ogg_to_wav_in_directory(directory)
    delete_ogg_files_in_directory(directory)


if __name__ == "__main__":
    main()
