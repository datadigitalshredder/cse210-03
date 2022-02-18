class Parachute:
    """A sketch drawing of the parachute and the jumper.

    The responsibility of Parachute is to keep track of the number of lines the jumper has left when guessing the word.
   
    Attributes:
        parachute (string): The number of lines on the parachute
    """

    def __init__(self):
        """Constructs a new instance of Parachute.

        Args:
            self (parachute): An instance of Parachute.
        """
        self._parachute = [' ___', '/   \\', ' ———', '\\   /', ' \\ / ', '  0', '/ | \\', ' / \\', " ", "^^^^^^^^^^^^^"]

    def cut_chute(self):
        """Cuts a line on the parachute if the guess is not correct, kills the jumper if no parachute is left

        Args:
            self (Parachute): An instance of Parachute.
        """
        self._parachute.pop(0)
        if self.parachute_life() == False:
            self._parachute[0] = '  X'
    
    def print_parachute(self):
        """Displays the number of lines left on the parachute

        Args:
            self (Parachute): An instance of Parachute.
        """
        for line in self._parachute:
            print(line)

    def parachute_life(self):
        """Life of the parachute for words, in this case, five letters in length. If more than five guesses are made, there will be no more life.

        Args:
            self (Parachute): An instance of Parachute.
        """
        if len(self._parachute) > 5:
            return True
        else:
            return False
