class ParserFindTagException(Exception):
    def __init__(self, messsage: str):
        self.message = messsage

    def __str__(self):
        return f'Ошибка - {self.message}'