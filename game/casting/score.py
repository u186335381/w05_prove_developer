from game.casting.actor import Actor


class Score(Actor):
    """
    A record of points made or lost. 

    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """

    def __init__(self, player_name, position):
        """Constructs a new Score."""
        super().__init__()
        self._player_name = player_name
        self._points = 0
        self._position = position
        self.add_points(0)

    def add_points(self, points):
        """Adds the given points to the score's total points.

        Args:
            points (int): The points to add.
        """
        self._points += points
        self.set_text(f"{self._player_name}: {self._points}")

    def get_player_name(self):
        """Gets the name of the player unto whom the points belong.

        Returns:
            string: The name of the player unto whom the points belong
        """
        return self._player_name

    def set_player_name(self, _player_name):
        """Adds the player name to whom the points belong.

        Args:
            _player_name (string): The name of the owner of the points.
        """
        self._player_name = _player_name

    def get_position(self):
        """Gets the position where the score will be displayed.

        Returns:
            string: The position where the score will be displayed.
        """
        return self._position

    def set_position(self, _position):
        """Adds the position where the score will be displayed.

        Args:
            _player_name (string): The position where the score will be displayed.
        """
        self._position = _position
