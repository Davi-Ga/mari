import pyttsx3

engine=pyttsx3.init()

def sound_out(output):
    engine.say(output)
    engine.runAndWait()