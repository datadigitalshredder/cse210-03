from game.wordblanks import WordBlanks
from game.wordgenerator import UnknownWordGenerator
from game.parachute import Parachute


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _blanks: dashed line for the blank word.
        generator: random selector of a word from the given list.
        stick_figure: draws the parachute
    """
    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._blanks = WordBlanks()
        self.generator = UnknownWordGenerator()
        self.stick_figure = Parachute()
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.stick_figure.parachute_life() == True and self._blanks.checker() == False:
            self._blanks.print_blanks()
            self.stick_figure.print_parachute()
            if self._blanks.guess_letter(self.generator.get_unknown_word()) == False:
                self.stick_figure.cut_chute()
        self._blanks.print_blanks()
        self.stick_figure.print_parachute()
