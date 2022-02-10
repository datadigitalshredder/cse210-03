import random

class UnknownWordGenerator:
    def __init__(self):
        bank = ['areas', 'pizza', 'trees']
        self._unknown_word = bank[random.randint(0, 2)]
    def get_unknown_word(self):
        return self._unknown_word
