class Console:
    """
    The responsibility of this class is to get text input and display text output.
    It also validates and return the letters chosen by the user.

    Stereotype:
        Service Provider, Interfacer

    Attributes:
        prompt (string): The prompt to display on each line.
        word_interface: The underscores with letters that represents the word to guess
        para_interface: The ascii interface of the parachute.
    """
    def __init__(self):
        self.letters = []


    def validate_letter(self, letter):
        """Validates the letter received from the user

        Args: 
            self (Screen): An instance of Screen.
            letter (string): The letter to validate

        Returns:
            string: The letter validated or an error
        """
        if letter.isalpha():
            if len(letter) == 1:
                if letter in self.letters:
                    return 3 #Error 3: Letter is repeated
                else:
                    # If there is no error
                    self.letters.append(letter)
                    return letter
            else:
                return 2 #Error 2: Letter is more than one letter
        else:
            return 1 #Error 1: Letter is a number or symbol
        
    def write(self, text):
        """Displays the given text on the screen. 

        Args: 
            self (Screen): An instance of Screen.
            text (string): The text to display.
        """
        print(text)