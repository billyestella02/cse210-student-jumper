import random

class Puzzle:
    """A code template for the puzzle that generates the word to be guessed,
       and checks if the guess is right.
    
    Stereotype:
        Information Holder

    Attributes:
        puzzle_list (list): The list of words where the guess will come from
        puzzle_to_guess (string): Randomly picked word to be guessed
        answer (list): The player's answer to the guess
        guess_letter (string): The letter guessed each round
    """
    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.

        Args:
            self (Puzzle): An instance of Puzzle.
        """
        self.puzzle_list = ['piano', 'spear', 'mother', 'broken', 'blanket', 'explain']
        self.puzzle_to_guess = self.puzzle_list[random.randint(0, len(self.puzzle_list) - 1)]
        self.answer = ['_'] * len(self.puzzle_to_guess)
        self.guess_letter = ''

    def get_puzzle(self):
        """Get the unanswered puzzle in text format

        Args:
            self (Puzzle): An instance of Puzzle.
        
        Returns:
            string: Blank answer in text format.
        """ 
        puzzle = ''.join(self.answer)
        return puzzle

    def check_guess(self, guess):
        """Check if guess is correct.

        Args:
            self (Player): An instance of Player.
            guess (string): The guessed letter
        
        Returns:
            boolean: True if guess is right, False otherwise.
        """ 
        if guess in self.puzzle_to_guess:
            self.guess_letter = guess
            return True
        else:
            return False

    def update_puzzle_to_guess(self):
        """Updates the blank answer text with the correct letter
           in the correct index.

        Args:
            self (Player): An instance of Player.
        """ 
        #print(self.puzzle_to_guess)
        puzzle = ''.join(self.answer)
        i = self.puzzle_to_guess.find(self.guess_letter)
        #print(i)
        #print(self.guess_letter)
        self.answer[i] = self.guess_letter 
    
    def is_guess_success(self):
        """Checks if letters in the answer are all guessed correctly.

        Args:
            self (Player): An instance of Player.
        
        Returns:
            boolean: True if guess is right, False otherwise.
        """ 
        if '_' not in self.answer:
            return True
        else:
            return False
