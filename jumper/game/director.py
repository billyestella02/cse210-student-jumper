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
            user_letter = self.guesser.ask_letter()
            
