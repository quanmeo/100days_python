class Question(object):
    ''' A question model '''
    def __init__(self, text, answer):
        self.__text = text
        self.__answer = answer

    def answer(self):
        return self.__answer

    def text(self):
        return self.__text
