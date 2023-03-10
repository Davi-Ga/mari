import datetime
from random import choice

class SystemInfo:
    def __init__():
        pass
    
    @staticmethod
    def exit_app():
        return "Desligando"
    
    @staticmethod
    def get_time():
        now=datetime.datetime.now()
        answer= f'Agora são {now.hour} horas e {now.minute} minutos'
        return answer
    
    @staticmethod
    def get_date():
        now=datetime.datetime.now()
        answer= f'Hoje é dia {now.day} de {now.month} de {now.year}'
        return answer
    
    @staticmethod
    def error_list():
        errors_list = [
            "MARI não conseguiu te ouvir",
            "MARI pediu para você repetir",
            "Desculpe, MARI não entendeu o que você disse",
            "MARI não entendeu o que você disse, por favor repita",
            "MARI está com dificuldades para entender o que você disse",
            "MARI está tentando compreender",
            "Por favor repita, MARI não entendeu",
        ]
        return choice(errors_list)