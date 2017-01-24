from config import FieldType
from copy import deepcopy
import config


#TODO Knoten korrekt löschen
#( Methode fuer finalen Pfad. Rueckwaerts von Zielknoten aus ueber Vorgaenger. )

class Node:

    def __init__(self, field_type, distance):
        self.field_type = field_type
        self.distance = distance
        self.visited = False
        self.predecessor = None
        self.neighbours = []


class Graph:

    def __init__(self):
        self.length = config.CELL_COUNT[0]
        self.width = config.CELL_COUNT[1]
        self.nodes = __empty_nodes__(self.length, self.width)

    def set_start_node(self, x, y):
        self[(x, y)].field_type = FieldType.start
        self[(x, y)].distance = 0

    def min_distance_unvisited(self):
        unvisited_nodes = filter(lambda x: not x.visited, self.nodes)
        return min(unvisited_nodes, key=lambda  x: x.distance)

    def __getitem__(self, pos):
        x, y = pos
        return self.nodes[x][y]


def __empty_nodes__(length, width):
    empty_node = Node(FieldType.normal, 100000)
    nodes = [[deepcopy(empty_node) for _ in range(length)] for _ in range(width)]
    nodes = __set_all_neighbours__(nodes)
    return nodes


def __set_all_neighbours__(_nodes):
    nodes = deepcopy(_nodes)
    for x, row in enumerate(nodes):
        for y, node in enumerate(row):
            neighbours = [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]
            for n in neighbours:
                if n[0] in range(len(nodes)) and n[1] in range(len(row)):
                    node.neighbours.append(nodes[n[0]][n[1]])
    return nodes



