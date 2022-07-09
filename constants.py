from game.shared.color import Color
from game.shared.point import Point


COLUMNS = 40
ROWS = 20
CELL_SIZE = 15
MAX_X = 900
MAX_Y = 600
FRAME_RATE = 1
FONT_SIZE = 15
CAPTION = "Cycle"
CYCLE_LENGTH = 1
WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)
YELLOW = Color(255, 255, 0)
GREEN = Color(0, 255, 0)
SCORE_POSITION_1 = Point(0, 0)
SCORE_POSITION_2 = Point(MAX_X - 150, 0)
CYCLE_POSITION_1 = Point(MAX_X - 600, 280)
CYCLE_POSITION_2 = Point((MAX_X - 240), 280)