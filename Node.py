from config import FieldType
from copy import deepcopy
import config
import itertools as it


#TODO Knoten korrekt loeschen

class Node:

    def __init__(self, field_type, distance):
        self.field_type = field_type
        self.distance = distance
        self.visited = False
        self.predecessor = None
        self.neighbours = []
        self.x = 0
        self.y = 0


class Graph:

    def __init__(self):
        self.length = config.CELL_COUNT[0]
        self.width = config.CELL_COUNT[1]
        self.nodes = self.__empty_nodes__()
        self.__set_all_neighbours__()

    def set_start_node(self, x, y):
        self[(x, y)].field_type = FieldType.start
        self[(x, y)].distance = 0

    def min_distance_unvisited(self, func):
        unvisited_nodes = filter(lambda x: not x.visited, self.nodes)
        unvisited_nodes = map(func, unvisited_nodes)
        return min(unvisited_nodes, key=lambda x: x.distance)

    #Marks the path backwards. Pass the ends PREDECESSOR!!
    def mark_path(self, node):
        if node.field_type != FieldType.start:
            node.field_type = FieldType.path
            self.mark_path(node.predecessor)

    def coords_to_index(self, x, y):
        return (self.width * y) + x

    def index_to_coords(self, i):
        return i % self.length, i/self.width

    def __empty_nodes__(self):
        empty_node = Node(FieldType.normal, 100000)
        nodes = [deepcopy(empty_node) for _ in range(self.length * self.width)]
        for i, n in enumerate(nodes):
            n.x, n.y = self.index_to_coords(i)
        return nodes

    def __set_all_neighbours__(self):
        neighbours = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        for n in self.nodes:
            neighbour_coords = map(lambda (x, y): (n.x + x, n.y + y), neighbours)
            neighbour_coords = filter(lambda c: c in list(it.product(range(self.length), range(self.width))), neighbour_coords)
            n.neighbours.extend(neighbour_coords)

    def __getitem__(self, item):
        if type(item) is tuple or list:
            item = self.coords_to_index(item[0], item[1])
        return self.nodes[item]
