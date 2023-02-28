import speech_recognition as sr
from queue import Queue
from threading import Thread
from random import choice
from speaker import sound_out
language = 'pt-BR'

rec = sr.Recognizer()
audio_queue = Queue()
def recognize_worker():
    errors_list = [
    "MARI could not understand audio",
    "MARI asked you to repeat",
    "Sorry, MARI could not understand what you said",
    ]
    
    while True:
        audio=audio_queue.get()
        if audio is None:
            break
        try:
            inpt=rec.recognize_google(audio,language=language,show_all=False,with_confidence=True)
            audio_queue.task_done()
            return "{}".format(inpt)
            #print("MARI thinks you said: " + rec.recognize_google(audio,language=language))
        
        except sr.UnknownValueError:
            return choice(errors_list)
        except sr.RequestError as e:
            return ("Could not request results from MARI service;- {0}").format(e)

recognize_thread=Thread(target=recognize_worker)
recognize_thread.daemon = True
recognize_thread.start()

with sr.Microphone() as source:
    rec.adjust_for_ambient_noise(source)
    try:    
        print("MARI is listening...")
        while True:
            audio_queue.put(rec.listen(source))
            response=recognize_worker()
            sound_out(response)
    except KeyboardInterrupt:
        pass    

audio_queue.join()
audio_queue.put(None)
recognize_thread.join()


