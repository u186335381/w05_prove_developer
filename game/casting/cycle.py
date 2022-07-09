import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Cycle(Actor):
    """
    A long line that can move in the Game.

    The responsibility of Cycle is to move itself and to avoid collision with another Cycle in order to win the game.

    Attributes:
        _segments ([Actor]): The number of elements that will belong to this cycle (How long its tail will be).
        _color (Color): The color of the text.
        _position (Point): The screen coordinates.
    """

    def __init__(self, color, initial_position):
        """Constructs a new Cycle."""
        super().__init__()
        self._segments = []
        self._color = color
        self._position = initial_position
        self._prepare_body()

    def get_segments(self):
        """Gets the Cycle's segments as List.

        Returns:
            [Actor]: The Cycle's segments.
        """
        return self._segments

    def move_next(self):
        """Moves the Cycle to its next position according to its velocity"""
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        """Gets one Cycle's segment at index 0.

        Returns:
            Actor: The Cycle's segment at index 0.
        """
        return self._segments[0]

    def grow_tail(self, number_of_segments):
        """ It adds new segments to the end of the Cycle's body."""
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)

            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(self._color)
            self._segments.append(segment)

    def turn_head(self, velocity):
        """The direction of he Cycle is changed if required."""
        self._segments[0].set_velocity(velocity)

    def _prepare_body(self):
        """ The creation of the body of the Cycle once it has been initialized."""
        x = self._position.get_x()
        y = self._position.get_y()

        for i in range(constants.CYCLE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "8" if i == 0 else "#"

            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(self._color)
            self._segments.append(segment)
