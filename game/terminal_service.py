

class TerminalService:
    """Manages input and output of the terminal
    """

    def read_text(self, text):
        """Reads text input from the terminal

        :param text: the text received
        :return: the input from the user
        """
        return input(text)

    def write_text(self, text):
        """Writes text to the terminal

        :param text: the text to display
        """
        print(text)
