import os
from pydub import AudioSegment

wavset = ['chunk-00.wav','chunk-01.wav']

wavs = [AudioSegment.from_wav(wav) for wav in wavset]
combined = wavs[0]

for wav in wavs[1:]:
    combined = combined.append(wav)

combined.export(os.path.join(os.path.dirname(__file__), "output.wav"), format="wav")
