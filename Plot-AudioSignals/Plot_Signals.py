from vad import VoiceActivityDetector
import json

filename = '6TU5302374.wav'
v = VoiceActivityDetector(filename)
v.plot_detected_speech_regions()



def save_to_file(data, file):
    with open(file, 'w') as fp:
        json.dump(data, fp)



v = VoiceActivityDetector(filename)
raw_detection = v.detect_speech()
print(raw_detection)
speech_labels = v.convert_windows_to_readible_labels(raw_detection)

save_to_file(speech_labels, "bala.json")
