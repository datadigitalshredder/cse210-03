import random

class UnknownWordGenerator:
    """A generator to randomly select a word from the a list.

    The responsibility of UnknownWordGenerator is to generate a random word for the jumper ot guess.
   
    Attributes:
        unknown_word (string): A randomly selected word.
    """
    def __init__(self):
        """Constructs a new instance of UnknownWordGenerator.

        Args:
            self (unknown_word): An instance of UnknownWordGenerator.
        """
        bank = ['areas', 'pizza', 'trees']
        self._unknown_word = bank[random.randint(0, 2)]
    def get_unknown_word(self):
        """Generates random word.

        Args:
            self (UnknownWordGenerator): An instance of UnknownWordGenerator.
        """
        return self._unknown_word
