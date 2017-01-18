from config import FieldType

class Node:
    def __init__(self, posX, posY, field_type, distance):
        self.posX = posX
        self.posY = posY
        self.field_type = field_type
        self.distance = distance
        self.predecessor = None
        self.neighbours = []
