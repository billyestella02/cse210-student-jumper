from game.console import Console
from game.puzzle import Puzzle
from game.player import Player

class Director:
    def __init__(self):
        self.console = Console()
        self.player = Player()
        self.puzzle = Puzzle()
        self.guess_is_right = False
        self.keep_playing = True
        
    
    def start_game(self):
        while self.keep_playing:
            self.get_input_output()
            self.do_updates() 
        self.game_over_output()
    
    def get_input_output(self):
        self.console.write(self.puzzle.get_puzzle())
        print()
        self.console.write(self.player.get_player_ascii())
        guess = self.console.read('Guess a letter [a-z]: ')
        self.guess_is_right = self.puzzle.check_guess(guess)
    
    def do_updates(self):
        if self.guess_is_right:
            self.puzzle.update_puzzle_to_guess()
            if self.puzzle.is_guess_success():
                self.keep_playing = False
        else:
            self.player.remove_parachute_line()
            if not self.player.is_alive():
                self.keep_playing = False

    def game_over_output(self):
        self.console.write(self.puzzle.get_puzzle())
        self.console.write(self.player.get_player_ascii())
