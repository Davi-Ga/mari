import speech_recognition as sr
from queue import Queue
from threading import Thread
language = 'pt-BR'

rec = sr.Recognizer()
audio_queue = Queue()

def recognize_worker():
        
    while True:
        audio=audio_queue.get()
        if audio is None:
            break
        try:
            print("MARI thinks you said " + rec.recognize_google(audio))
        
        except sr.UnknownValueError:
            print ("MARI could not understand audio")
        except sr.RequestError as e:
            print ("Could not request results from MARI service; {0}").format(e)
        
        audio_queue.task_done()

recognize_thread = Thread(target=recognize_worker)
recognize_thread.daemon = True
recognize_thread.start()

with sr.Microphone() as source:
    sr.adjust_for_ambient_noise(source)
    try:
        while True:
            audio = rec.listen(source)
            audio_queue.put(audio)
    except KeyboardInterrupt:
        pass    

audio_queue.join()
audio_queue.put(None)
recognize_thread.join()