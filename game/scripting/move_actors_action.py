from game.scripting.action import Action


class MoveActorsAction(Action):
    """
    It excecutes the move_next method in all the actors in the cast received as input parameter, it allows the actors to move to its next position. 
    """

    def __init__(self):
        """Constructs a new MoveActorsAction."""
        pass

# Override the execute(cast, script) method as follows:
    def execute(self, cast, script):
        actors = cast.get_all_actors()
        for actor in actors:
            actor.move_next()
