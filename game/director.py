from terminal_service import TerminalService
from parachute import Parachute
from word import Word


class Director:
    """Controls the play of the game

    Attributes:
        _terminal_service: reads and writes from/to the terminal
        _parachute: represents and manages the lives of the player
        _word: the secret word and the associated guesses and comparisons
    """

    def __init__(self):
        """Constructs new Director

        Args:
            self: the Director instance
        """
        self._is_playing = True
        self._terminal_service = TerminalService()
        self._parachute = Parachute()
        self._word = Word()

    def start_game(self):
        """Runs the loop of the game
        """
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """Gets input from user to be used in-game
        """
        pass

    def _do_updates(self):
        """Performs updates to the game based on user input
        """
        pass

    def _do_outputs(self):
        """Outputs results from input including win message
        """
        pass
