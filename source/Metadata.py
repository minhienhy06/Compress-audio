import os
import json
import soundfile as sf
import numpy as np
import librosa

Metadata_path = "../dataset/metadata.json"


def calculate_snr(original_path, compressed_path):
    x, sr = librosa.load(original_path, sr=None)
    x_hat, _ = librosa.load(compressed_path, sr=sr)
    n = min(len(x), len(x_hat))
    x = x[:n]
    x_hat = x_hat[:n]
    noise = x - x_hat
    signal_power = np.sum(x ** 2)
    noise_power = np.sum(noise ** 2)
    if noise_power == 0:
        return float("inf")
    return 10 * np.log10(signal_power / noise_power)

def Make_metadata():
    files = os.listdir("../dataset/original")
    data = {}
    for file in files :
        name = file.replace(".wav","")
        path_original = os.path.join("../dataset/original" ,name+ ".wav")
        path_lossless = os.path.join("../dataset/lossless" ,name+ ".flac")
        path_lossy = os.path.join("../dataset/lossy" ,name + ".mp3")
        size_original = os.path.getsize(path_original)/1e6
        size_lossless = os.path.getsize(path_lossless)/1e6
        size_lossy = os.path.getsize(path_lossy)/1e6
        ori_info = sf.info(path_original)
        lossless_info = sf.info(path_lossless)
        lossy_info = sf.info(path_lossy)
        duration = ori_info.duration

        snr_lossless = calculate_snr(path_original, path_lossless)
        snr_lossy = calculate_snr(path_original, path_lossy)
        if np.isinf(snr_lossless):
            snr_lossless = "Perfect (Inf)"
        else:
            snr_lossless = round(snr_lossless)
        if np.isinf(snr_lossy):
            snr_lossy = "Perfect (Inf)"
        else:
            snr_lossy = round(snr_lossy)

        
        data[name] = {
            "paths" :{
                "original" : path_original,
                "lossless" : path_lossless,
                "lossy" : path_lossy,

            },
            "sizes" : {
                "size_original" : f"{size_original:.2f} MB",
                "size_lossless" : f"{size_lossless:.2f} MB",
                "size_lossy" : f"{size_lossy:.2f} MB",

            },
            "info" : {
                "sampe_rate" : ori_info.samplerate,
                "channels" : ori_info.channels,
                "bit_depth_ori" : ori_info.subtype,
                "bit_depth_lossless" : lossless_info.subtype,
                "bit_depth_lossy" : lossy_info.subtype,
                

            },

            "evaluation": {
                "lossless_compressrate" : round(size_original / size_lossless),
                "lossy_compressrate" : round(size_original / size_lossy),
                "bitrate_ori" : round((size_original * 8 * 1e6)/ (duration *1000)),
                "bitrate_losless" : round((size_lossless * 8 *1e6)/ ( duration *1000)),
                "bitrate_lossy" :round ((size_lossy * 8 *1e6)/ (duration *1000)),
                "lossless_snr": snr_lossless,
                "lossy_snr": snr_lossy,

            },
            
            
            
        }



    with open(Metadata_path,"w") as w:
        json.dump(data, w, indent = 5)
        print("success save")



if __name__ == "__main__":
    Make_metadata()


