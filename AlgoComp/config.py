from enum import Enum   # package: enum34


# Configuration
VISUALBOARD_SIZE = (400, 400)
CELL_COUNT = (10, 10)   # only quadratic values!
SPEED = 100  # pause between steps in milliseconds
OBSTACLE_COUNT = 30
MAX_DISTANCE = 10000


class FieldType(Enum):
    normal = 0
    start = 1
    end = 2
    current = 3
    obstacle = 4
    path = 5
