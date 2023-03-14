import speech_recognition as sr
from queue import Queue
from threading import Thread
from speaker import sound_out
from core import SystemInfo

rec = sr.Recognizer()
audio_queue = Queue()

def recognize_worker():
    
    while True:
        audio=audio_queue.get()
        if audio is None:
            break
        try:
            inpt=rec.recognize_google(audio,language="pt-BR")
            return f"{inpt}"
        
        except sr.UnknownValueError:
            return f"{SystemInfo.error_list()}"
        except sr.RequestError as e:
            return f"Não conseguimos resultados com o serviço da MARI;- {e}"

recognize_thread=Thread(target=recognize_worker)
recognize_thread.daemon = True
recognize_thread.start()

inicio="MARI está ouvindo..."
print(inicio)
sound_out(inicio)

with sr.Microphone() as source:
    
    rec.adjust_for_ambient_noise(source)
    try:    
        while True:
            audio_queue.put(rec.listen(source))
            response=recognize_worker()
            print("{}".format(response))
            
            if response is not None:
                text=response['text']
                
            if response =="que horas sao" or response=="Que horas são":
                sound_out(SystemInfo.get_time())
                pass
                
            sound_out(response)
            
            audio_queue.task_done()
            
    except KeyboardInterrupt:
        pass
    
audio_queue.join()
audio_queue.put(None)
recognize_thread.join()   



