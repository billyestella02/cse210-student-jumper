class Player:
    def __init__(self):
        self.player_ascii = ['  ___ \n', ' /___\\\n', ' \\   /\n', '  \\ / \n', '   0  \n', '  /|\\ \n', '  / \\ \n', '\n^^^^^^^\n']
    
    def get_player_ascii(self):
        player = ''.join(self.player_ascii)
        return player

    def remove_parachute_line(self):
        if len(self.player_ascii) > 4:
            del self.player_ascii[0]
        else:
            self.player_ascii[0] = '\n   X  \n'
    
    def is_alive(self):
        if self.player_ascii[0] == '\n   X  \n':
            return False
        else:
            return True

