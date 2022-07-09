import constants

from game.casting.cast import Cast
from game.casting.score import Score
from game.casting.cycle import Cycle
from game.scripting.script import Script
from game.scripting.control_first_player_action import ControlFirstPlayerAction
from game.scripting.control_second_player_action import ControlSecondPlayerAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point


def main():

    # create the cast
    cast = Cast()
    cast.add_actor("cycle_player_1", Cycle(constants.RED, constants.CYCLE_POSITION_1))
    cast.add_actor("cycle_player_2", Cycle(constants.GREEN, constants.CYCLE_POSITION_2))
    cast.add_actor("score_player_1", Score("Player One", constants.SCORE_POSITION_1))
    cast.add_actor("score_player_2", Score("Player Two", constants.SCORE_POSITION_2))

    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    # We add all the actions to be performed during gameplay
    script = Script()
    script.add_action("input", ControlFirstPlayerAction(keyboard_service))
    script.add_action("input", ControlSecondPlayerAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))

    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()
