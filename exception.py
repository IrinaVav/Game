class BoardException(Exception):
    pass

class BoardOut(BoardException):
    def __str__(self):
        return 'Координаты выходят за поле!'

class BoardUsed(BoardException):
    def __str__(self):
        return 'Вы уже стреляли в эту клетку! Повторите ввод координат!'
