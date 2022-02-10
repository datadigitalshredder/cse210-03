class WordBlanks:

    def __init__(self):
        self.blankString = list("_ _ _ _ _")
    #def for a guess, take input from Director.
    def guess_letter(self, unknown_word):
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
        if "_" in self.blankString:
            return False
        else:
            return True


    def print_blanks(self):
        print("".join(self.blankString))
        print("")
    #returns inputs