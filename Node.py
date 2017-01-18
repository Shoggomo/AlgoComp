from config import FieldType

//Distanz zu Beginn bei Startknoten 0.
//Methode für Knoten mit geringster Distanz unter den unbesuchten Knoten.
//Methode für finalen Pfad. Rückwärts von Zielknoten aus über Vorgänger.

class Node:
    def __init__(self, posX, posY, field_type, distance):
        self.posX = posX
        self.posY = posY
        self.field_type = field_type
        self.distance = distance
        self.predecessor = None
        self.neighbours = []
