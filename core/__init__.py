import datetime
from random import choice

class SystemInfo:
    def __init__():
        pass
    
    def exit_app():
        return "Desligando",exit()
    
    def get_time():
        now=datetime.datetime.now()
        answer= f'Agora são {now.hour} horas e {now.minute} minutos'
        return answer
    
    def error_list():
        errors_list = [
            "MARI não conseguiu te ouvir",
            "MARI pediu para você repetir",
            "Desculpe, MARI não entendeu o que você disse",
            "MARI não entendeu o que você disse, por favor repita",
        ]
        return choice(errors_list)