from enum import Enum   #package: enum34


#Configuration
VISUALBOARD_SIZE = (500, 500)
CELL_COUNT = (10, 10)

class FieldType(Enum):
    unvisited = 0
    visited = 1
    start = 2
    end = 3
    current = 4
    obstacle = 5
    path = 6
