from game.console import Console
from game.puzzle import Puzzle
from game.player import Player

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        console (Console): An instance of the class of objects known as Console.
        player (Player): An instance of the class of objects known as Player.
        puzzle (Puzzle): An instance of the class of objects known as Puzzle.
        guess_is_right (boolean): Whether or not the guess is right or wrong.
        keep_playing (boolean): Whether or not the game can continue.
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.console = Console()
        self.player = Player()
        self.puzzle = Puzzle()
        self.guess_is_right = False
        self.keep_playing = True
        
    
    def start_game(self):
        """Starts the game and ends it if requirements are met.

        Args:
            self (Director): an instance of Director.
        """
        while self.keep_playing:
            self.get_input_output()
            self.do_updates() 
        self.game_over_output()
    
    def get_input_output(self):
        """Gets the inputs at the beginning of each round of play. 
        Output is also included since code structure will be the same.

        Args:
            self (Director): An instance of Director.
        """
        self.console.write(self.puzzle.get_puzzle())
        print()
        self.console.write(self.player.get_player_ascii())
        guess = self.console.read('Guess a letter [a-z]: ')
        self.guess_is_right = self.puzzle.check_guess(guess)
    
    def do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, check if the guess is right or wrong.

        Args:
            self (Director): An instance of Director.
        """
        if self.guess_is_right:
            self.puzzle.update_puzzle_to_guess()
            if self.puzzle.is_guess_success():
                self.keep_playing = False
        else:
            self.player.remove_parachute_line()
            if not self.player.is_alive():
                self.keep_playing = False

    def game_over_output(self):
        """Displays output once game is over, depending on the result.
        Show the guessed word if done, change player appearance if parachute
        gets completely broken.
        
        Args:
            self (Director): An instance of Director.
        """
        self.console.write(self.puzzle.get_puzzle())
        self.console.write(self.player.get_player_ascii())
