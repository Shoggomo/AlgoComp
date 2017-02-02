from enum import Enum   #package: enum34


#Configuration
VISUALBOARD_SIZE = (500, 500)
CELL_COUNT = (10, 10)   # only quadratic values!
SPEED = 200 #pause between steps


class FieldType(Enum):
    normal = 0
    start = 1
    end = 2
    current = 3
    obstacle = 4
    path = 5
