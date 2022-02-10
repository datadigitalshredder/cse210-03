from game.wordblanks import WordBlanks
from game.wordgenerator import UnknownWordGenerator
from game.parachute import Parachute


class Director:
    #holds all the defs and directs the game
    def __init__(self):
        
        return
    def start_game(self):
        self._blanks = WordBlanks()
        generator = UnknownWordGenerator()
        stick_figure = Parachute()
        while stick_figure.parachute_life() == True and self._blanks.checker() == False:
            self._blanks.print_blanks()
            stick_figure.print_parachute()
            if self._blanks.guess_letter(generator.get_unknown_word()) == False:
                stick_figure.cut_chute()
        self._blanks.print_blanks()
        stick_figure.print_parachute()
