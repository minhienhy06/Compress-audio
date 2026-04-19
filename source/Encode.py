import os
from pydub import AudioSegment 


def run_encoding():
    orig_dir = "../dataset/original"
    lossless_dir = "../dataset/lossless"
    lossy_dir = "../dataset/lossy"

    for folder in [lossless_dir, lossy_dir]:
        os.makedirs(folder, exist_ok=True)


    files = [f for f in os.listdir(orig_dir) if f.endswith(".wav")]

    for file_name in files:
        name_only = os.path.splitext(file_name)[0]
        
        input_path = os.path.join(orig_dir, file_name)
        
        audio = AudioSegment.from_wav(input_path)

        flac_path = os.path.join(lossless_dir, name_only + ".flac")
        audio.export(flac_path, format="flac")
        print(f"Exported Lossless: {flac_path}")

        mp3_path = os.path.join(lossy_dir, name_only + ".mp3")
        audio.export(mp3_path, format="mp3", bitrate="64k")
        print(f"Exported Lossy: {mp3_path}")

if __name__ == "__main__":
    run_encoding()

