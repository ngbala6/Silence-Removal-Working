# Import packages
from pydub import AudioSegment
from pydub.playback import play


# Play audio
playaudio = AudioSegment.from_file("Paste your File Name Here", format="wav")
play(playaudio)
