#Managing Audio Storage with Combined Lossy and Lossless Compression

## Structure 
Compression_projection/
 dataset/
  original/
  lossless/
  lossy/
 source/
  Encode.py
  Metadata.py
  Retrieval.py
  Main.py
 
 

## Requirement
- Python 3.12.3
- ffmpeg installed (needed for pydub encode/decode)

## Running

### Dataset
- download some wav audios into original

### Source
- run python3 Encode.py to let the code generate from original files to lossless and lossy file
- run python3 Metadata.py to write informations in metadata.json
- run python3 Main.py to sum all 2 aboves step in one 

#### Retrieval
- Retrieval_audio("name","quality") to show the metadata information and play the audio
- Spectrogram("name","quality") to show the spectrogram of the audio


## Further explainations
- You have to download some audios to analyze the audio
- Encode.py will access into lossless and lossy file and create files with .flac for lossless and .mp3 for lossy. FLAC is using linear prediction model, and MP3 is using the psychoacoustic masking
- Metadata.py will write all information in metadata.json, but first u have to write {} in metadata.json in order Metadata.json to write in. Metadata.py will access to the path and get each information of audio , and find the snr of the audio. I find this easier when calculate in Metadata.py when i have loop file in files then i can save information easier for each audio
- Main.py just call back Encode.py and Main.py to run 
- For interaction you go to Retrieval.ipynb. I think this interaction is easier in jupyter instead of python when i have some button to push. I make this similar to metadata logic, just go to the path and access to the audio. To run you just call the function again with "name" and "quality" then there will be a play button so you can play and hear the audio

## Authors
- Trần Minh Hiển
- Gemini
- Cursor 
I can not lie to myself if without these tools, it will be really hard for me to make this project. I feel really happy for this project, this is the very first project i do and upload to github. I promise in the future i will make more projects to dedicate to the world and use less AI tools for the support ( just support the milimal things, and i will do the hard things ).
