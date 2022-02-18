class WordBlanks:
    """A dashed line drawing of the word to guess.

    The responsibility of WordBlanks is to keep track of the correct letters when guessing the word.
   
    Attributes:
        blankString (string): The dashes of letters on the word.
    """

    def __init__(self):
        """Constructs a new instance of WordBlanks.

        Args:
            self (blankString): An instance of WordBlanks.
        """
        self._blankString = list("_ _ _ _ _")
    #def for a guess, take input from Director.
    def guess_letter(self, unknown_word):
        """Requires input from jumper to guess letter of the random word.

        Args:
            self (WordBlanks): An instance of WordBlanks.
        """
        guess = input("Guess a letter (a/z): ")
        if guess in unknown_word:
            index = 0
            for letter in unknown_word:
                if letter == guess:
                    self._blankString [index *2] = guess
                index += 1
            return True
        return False

    def checker(self):
        """Check input from jumper against the random word.

        Args:
            self (WordBlanks): An instance of WordBlanks.
        """
        if "_" in self._blankString:
            return False
        else:
            return True


    def print_blanks(self):
        """Prints the letter from jumper if correct, otherwise prints none.

        Args:
            self (WordBlanks): An instance of WordBlanks.
        """
        print("".join(self._blankString))
        print("")
    #returns inputs