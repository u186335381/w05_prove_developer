import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point


class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.

    The responsibility of HandleCollisionsAction is to handle the situation when the Cycles collide with themselves or with another Cycle, or when the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
        _is_draw (boolean): Whether or not the game ended by draw.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._is_draw = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_tail_growing(cast)
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)

    def _handle_tail_growing(self, cast):
        """Adds a new segment to the end of each of the Cycles in the game."""
        cycle_player_1 = cast.get_first_actor("cycle_player_1")
        cycle_player_2 = cast.get_first_actor("cycle_player_2")
        cycle_player_1.grow_tail(1)
        cycle_player_2.grow_tail(1)

    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the Cycles collides with one of its segments or with the opponent's segments.
        It also checks if both Cycles have collisioned at the same tame to display a Draw message.

        Args:
            cast (Cast): The cast of Actors in the game.
        """
        # We get the first player's cycle
        cycle_player_1 = cast.get_first_actor("cycle_player_1")
        head_player_1 = cycle_player_1.get_segments()[0]
        segments_player_1 = cycle_player_1.get_segments()[1:]

        # We get the second player's cycle
        cycle_player_2 = cast.get_first_actor("cycle_player_2")
        head_player_2 = cycle_player_2.get_segments()[0]
        segments_player_2 = cycle_player_2.get_segments()[1:]

        is_player_1_winner = False
        is_player_2_winner = False

        # We check if they collide with one another or with themselves
        for segment_player_1 in segments_player_1:
            if head_player_1.get_position().equals(segment_player_1.get_position()):
                self._is_game_over = True
                cast.get_first_actor("score_player_2").add_points(1)
                is_player_2_winner = True
            elif head_player_2.get_position().equals(segment_player_1.get_position()):
                self._is_game_over = True
                cast.get_first_actor("score_player_1").add_points(1)
                is_player_1_winner = True

        for segment_player_2 in segments_player_2:
            if head_player_2.get_position().equals(segment_player_2.get_position()):
                self._is_game_over = True
                cast.get_first_actor("score_player_1").add_points(1)
                is_player_1_winner = True
            elif head_player_1.get_position().equals(segment_player_2.get_position()):
                self._is_game_over = True
                cast.get_first_actor("score_player_2").add_points(1)
                is_player_2_winner = True

        # We check if their heads collide to end the game in a Draw.
        for segment_player_2 in segments_player_2:
            if head_player_2.get_position().equals(head_player_1.get_position()):
                self._is_game_over = True
                self._is_draw = True

        if is_player_1_winner and is_player_2_winner:
            self._is_draw = True

    def _handle_game_over(self, cast):
        """Shows the 'game over!' or 'Draw!' message and turns the Cycles white and stop counting points if the game is over.

        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            cycle_player_1 = cast.get_first_actor("cycle_player_1")
            segments_player_1 = cycle_player_1.get_segments()

            cycle_player_2 = cast.get_first_actor("cycle_player_2")
            segments_player_2 = cycle_player_2.get_segments()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            screen_message = ""
            if self._is_draw:
                screen_message = "Draw!"
            else:
                screen_message = "Game Over!"

            message = Actor()
            message.set_text(screen_message)
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment in segments_player_1:
                segment.set_color(constants.WHITE)

            for segment in segments_player_2:
                segment.set_color(constants.WHITE)
