import speech_recognition as sr
from queue import Queue
from threading import Thread
from random import choice
from speaker import sound_out
from config import *

rec = sr.Recognizer()
audio_queue = Queue()
def recognize_worker():
    
    while True:
        audio=audio_queue.get()
        if audio is None:
            break
        try:
            inpt=rec.recognize_google(audio,language="pt-BR")
            return "{}".format(inpt)
        
        except sr.UnknownValueError:
            return choice(errors_list)
        except sr.RequestError as e:
            return ("Não conseguimos resultados com o serviço da MARI;- {0}").format(e)

recognize_thread=Thread(target=recognize_worker)
recognize_thread.daemon = True
recognize_thread.start()

print("MARI está ouvindo...")
with sr.Microphone() as source:
    rec.adjust_for_ambient_noise(source)
    try:    
        while True:
            audio_queue.put(rec.listen(source))
            response=recognize_worker()
            print("Você disse: {}".format(response))
            
            if response in commands:
                mari_response = commands[response]
                response=mari_response
                print("MARI: {}".format(mari_response))
                
                if response == "desligando":
                    sound_out(response)
                    exit()   
            sound_out(response)
            
            audio_queue.task_done()
            
    except KeyboardInterrupt:
        pass
    
audio_queue.join()
audio_queue.put(None)
recognize_thread.join()   



