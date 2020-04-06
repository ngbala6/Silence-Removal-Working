from pydub import AudioSegment
from pydub.playback import play

sound = AudioSegment.from_file("6TU5302374.wav", format="wav")
play(sound)
