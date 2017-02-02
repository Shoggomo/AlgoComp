from config import FieldType
from copy import deepcopy
import itertools as it


class Graph:

    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.nodes = self.__empty_nodes__()
        self.__set_all_neighbours__()

    def set_start_node(self, x, y):
        self[(x, y)].field_type = FieldType.start
        self[(x, y)].distance = 0

    def set_end_node(self, x, y):
        self[(x, y)].field_type = FieldType.end

    def min_distance_unvisited(self, func):
        unvisited_nodes = filter(lambda x: x and not x.visited, self.nodes)
        if func:
            unvisited_nodes = map(func, unvisited_nodes)
        return min(unvisited_nodes, key=lambda x: x.distance)

    #Marks the path backwards. Pass the ends PREDECESSOR!!
    def mark_path(self, node):
        if node.field_type != FieldType.start:
            node.field_type = FieldType.path
            self.mark_path(node.predecessor)

    def delete_node(self, item):
        node = self[item]
        neighbours = node.neighbours
        self[item] = None
        map(lambda n: n.neighbours.remove(node), neighbours)

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
        relative_neighbour_coords = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        for n in self.nodes:
            neighbour_coords = map(lambda (x, y): (n.x + x, n.y + y), relative_neighbour_coords)
            neighbour_coords = filter(lambda c: c in list(it.product(range(self.length), range(self.width))), neighbour_coords)
            neighbour_nodes = [self[c] for c in neighbour_coords]
            n.neighbours.extend(neighbour_nodes)

    def __getitem__(self, item):
        if type(item) is tuple or type(item) is list:
            item = self.coords_to_index(item[0], item[1])
        return self.nodes[item]

    def __setitem__(self, item, value):
        if type(item) is tuple or type(item) is list:
            item = self.coords_to_index(item[0], item[1])
        self.nodes[item] = value


class Node:

    def __init__(self, field_type, distance):
        self.field_type = field_type
        self.distance = distance
        self.visited = False
        self.predecessor = None
        self.neighbours = []
        self.x = 0
        self.y = 0


def get_color_for_node(node):
    colors = {
        FieldType.normal: "white",
        FieldType.start: "blue",
        FieldType.end: "red",
        FieldType.current: "orange",
        FieldType.obstacle: "black",
        FieldType.path: "pink",
    }
    if node:
        if node.visited and node.field_type is FieldType.normal:
            return "green"
        return colors[node.field_type]
    return colors[FieldType.obstacle]


def graph_to_colormatrix(graph):
    color_matrix = []
    l = graph.length
    w = graph.width
    for x in range(l):
        color_matrix.append([])
        for y in range(w):
            node = graph[(x, y)]
            color_matrix[x].append(get_color_for_node(node))
    return color_matrix