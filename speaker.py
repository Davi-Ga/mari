import pyttsx3

engine=pyttsx3.init()

def sound_out(output):
    engine.say(output)
    
    voices=engine.getProperty('voices')
    volume=engine.getProperty('volume')
    
    engine.setProperty(volume,1)
    engine.setProperty('rate', 125) 
    engine.setProperty('voice', voices[1].id)
    engine.runAndWait()