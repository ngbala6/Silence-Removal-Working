import os
from pydub import AudioSegment
import glob

wavfiles  = glob.glob("./Need-to-Mergeaudio/*.wav")
print(wavfiles)

wavs = [AudioSegment.from_wav(wav) for wav in wavfiles]

combined = wavs[0]

for wav in wavs[1:]:
    combined = combined.append(wav)

combined.export(os.path.join(os.path.dirname(__file__), "./Merged-Audio/Mergedaudio.wav"), format="wav")
