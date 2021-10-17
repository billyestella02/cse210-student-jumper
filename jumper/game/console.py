class Console:
    """
    The responsibility of this class is to get text input and display text output.
    It also validates and return the letters chosen by the user.

    Stereotype:
        Service Provider, Interfacer

    Attribute:
        letters: A list containing the letters the user already tried to guess.
    """
    def __init__(self):
        self.letters = []

    def read(self, prompt):
        """Gets text input from the user through the screen.

        Args: 
            self (Screen): An instance of Screen.
            prompt (string): The prompt to display to the user.

        Returns:
            string: The user's input as text.
        """
        return input(prompt)

    def write(self, text):
        """Displays the given text on the screen. 

        Args: 
            self (Screen): An instance of Screen.
            text (string): The text to display.
        """
        print(text)

    def write_error(self, text):
        """Displays the given error on the screen. 

        Args: 
            self (Screen): An instance of Screen.
            text (string): The error to display.
        """
        print(f'\033[1;31;40m{text}\033[0;37;40m')
    
    def validate_letter(self, letter):
        """Validates the letter received from the user

        Args: 
            self (Screen): An instance of Screen.
            letter (string): The letter to validate

        Returns:
            string: The letter validated or a number of error
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