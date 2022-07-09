from game.scripting.action import Action


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.

    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.

        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        score_player_1 = cast.get_first_actor("score_player_1")
        score_player_2 = cast.get_first_actor("score_player_2")
        messages = cast.get_actors("messages")

        cycle_player_1 = cast.get_first_actor("cycle_player_1")
        segments_player_1 = cycle_player_1.get_segments()

        cycle_player_2 = cast.get_first_actor("cycle_player_2")
        segments_player_2 = cycle_player_2.get_segments()

        self._video_service.clear_buffer()
        self._video_service.draw_actors(segments_player_1)
        self._video_service.draw_actors(segments_player_2)
        self._video_service.draw_actor(score_player_1)
        self._video_service.draw_actor(score_player_2)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()
