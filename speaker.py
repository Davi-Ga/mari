import pyttsx3

engine=pyttsx3.init()
volume=engine.getProperty('volume')

engine.setProperty(volume,1)
engine.setProperty('rate', 170)
 
def sound_out(output):
    engine.say(output)
    
    engine.runAndWait()