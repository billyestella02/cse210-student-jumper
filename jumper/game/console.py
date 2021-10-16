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
     
    def validateLetter(self, letter):
        """Validates the letter received from the user

        Args: 
            self (Screen): An instance of Screen.
            prompt (string): The letter to validate

        Returns:
            string: The letter validated or an error
        """
        try:
            letter.isString()

    def read_number(self, prompt):
        """Gets numerical input from the user through the screen.

        Args: 
            self (Screen): An instance of Screen.
            prompt (string): The prompt to display to the user.

        Returns:
            float: The user's input as a float.
        """
        return float(input(prompt))
        
    def write(self, text):
        """Displays the given text on the screen. 

        Args: 
            self (Screen): An instance of Screen.
            text (string): The text to display.
        """
        print(text)