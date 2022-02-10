class Parachute:

    def __init__(self):
        self._parachute = [' ___', '/   \\', ' ———', '\\   /', ' \\ / ', '  0', '/ | \\', ' / \\', " ", "^^^^^^^^^^^^^"]

    def cut_chute(self):
        self._parachute.pop(0)
        if self.parachute_life() == False:
            self._parachute[0] = '  X'
    
    def print_parachute(self):
        for line in self._parachute:
            print(line)

    def parachute_life(self):
        if len(self._parachute) > 5:
            return True
        else:
            return False
