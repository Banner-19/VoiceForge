import requests
from TTS.api import TTS
import os

# Download a sample speaker file
speaker_wav_path = "/content/Narendra_Modi_voice.ogg-[AudioTrimmer.com].wav"

# Initialize TTS model
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=True)

# Generate speech by cloning the voice from the sample speaker
output_path = "gana.wav"
tts.tts_to_file(
    text="जब कोई बात बिगड़ जाए .....जब कोई मुश्क़िल पड़ जाए...........तुम देना साथ मेरा, ओ हमनवा............ना कोई है, ना कोई था, ज़िंदगी में तुम्हारे सिवा...............तुम देना साथ मेरा, ओ हमनवा..........तुम देना साथ मेरा, ओ हमनवा",
    file_path=output_path,
    speaker_wav=speaker_wav_path,
    language="hi"
)

print(f"Speech synthesis complete! Output saved at: {output_path}")
