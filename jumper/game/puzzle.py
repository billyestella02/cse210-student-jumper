import random

class Puzzle:
    def __init__(self):
        self.puzzle_list = ['piano', 'spear', 'mother', 'broken', 'blanket', 'explain']
        self.puzzle_to_guess = self.puzzle_list[random.randint(0, len(self.puzzle_list) - 1)]
        self.answer = ['_'] * len(self.puzzle_to_guess)
        self.guess_letter = ''

    def get_puzzle(self):
        puzzle = ''.join(self.answer)
        return puzzle

    def check_guess(self, guess):
        if guess in self.puzzle_to_guess:
            self.guess_letter = guess
            return True
        else:
            return False

    def update_puzzle_to_guess(self):
        #print(self.puzzle_to_guess)
        puzzle = ''.join(self.answer)
        i = self.puzzle_to_guess.find(self.guess_letter)
        #print(i)
        #print(self.guess_letter)
        self.answer[i] = self.guess_letter 
    
    def is_guess_success(self):
        if '_' not in self.answer:
            return True
        else:
            return False
