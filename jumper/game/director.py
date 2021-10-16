# from game.guesser import Guesser
from game.guesser import Guesser
from game.word_chooser import WordChooser
from game.console import Console

class Director:
    """
    The Director class will comunicate the other classes with eachother
    """

    def __init__(self):

        # self.guesser = Guesser
        self.word = ''
        self.keep_playing = True
        self.chooser = WordChooser()
        self.guesser = Guesser()
        self.console = Console()
    
    def start_game(self):

        self.word = self.chooser.choose_word()
        
        while self.keep_playing:
            user_letter = self.asking_letter()
            self.console.write(f'You chose the "{user_letter}" letter')

    def asking_letter(self):
        #parachute = self.parachute.get_parachute()
        #self.console.write(parachute)
        invalid_letter = True
        while invalid_letter:
            #The while loop only breaks when the user types a valid letter
            user_letter = input('Guess a letter [a-z]: ')
            letter = self.console.validate_letter(user_letter)
            invalid_letter = self.check_validation(letter)
        return letter

    def check_validation(self, console_answer):
        if console_answer == 1:
            self.console.write('The letter cannot contain numbers or symbols')
            return True
        elif console_answer == 2:
            self.console.write('You should type one letter only')
            return True
        elif console_answer == 3:
            self.console.write('You already wrote that letter')
            return True
        else:
            #There is no error with the letter
            return False


        

