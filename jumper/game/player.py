class Player:
    """A code template for the player in the appearance of a 
       parachute rider.
    
    Stereotype:
        Information Holder

    Attributes:
        player_ascii (list): The player with a parachute in ascii format.
    """
    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.

        Args:
            self (Player): An instance of Player.
        """
        self.player_ascii = ['  ___ \n', ' /___\\\n', ' \\   /\n', '  \\ / \n', '   0  \n', '  /|\\ \n', '  / \\ \n', '\n^^^^^^^\n']
    
    def get_player_ascii(self):
        """gets the player's appearance, in text form.

        Args:
            self (Player): An instance of Player.
        
        Returns:
            string: Player appearance in text format.
        """ 
        player = ''.join(self.player_ascii)
        return player

    def remove_parachute_line(self):
        """Updates the parachute's appearance if guess is wrong.

        Args:
            self (Player): An instance of Player.

        """ 
        if len(self.player_ascii) > 4:
            del self.player_ascii[0]
        else:
            self.player_ascii[0] = '\n   X  \n'
    
    def is_alive(self):
        """Checks if player still has his parachute.

        Args:
            self (Player): An instance of Player.
        
        Returns:
            boolean: True if player still has his parachute, False otherwise.
        """ 
        if self.player_ascii[0] == '\n   X  \n':
            return False
        else:
            return True


