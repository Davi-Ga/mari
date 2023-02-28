import speech_recognition as sr
from queue import Queue
from threading import Thread
from random import choice
from speaker import sound_out
from config import conversations,commands

rec = sr.Recognizer()
audio_queue = Queue()
def recognize_worker():
    errors_list = [
        "MARI não conseguiu te ouvir",
        "MARI pediu para você repetir",
        "Desculpe, MARI não entendeu o que você disse",
        "MARI não entendeu o que você disse, por favor repita",
    ]
    while True:
        audio=audio_queue.get()
        if audio is None:
            break
        try:
            inpt=rec.recognize_google(audio,language="pt-BR")
            audio_queue.task_done()
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
            
            mari_response = commands[response]
            sound_out(mari_response)
            print("MARI: {}".format(mari_response))
            
            
    except KeyboardInterrupt:
        pass    

audio_queue.join()
audio_queue.put(None)
recognize_thread.join()


