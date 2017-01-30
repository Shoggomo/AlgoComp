import copy
from Node import Node
from Node import Graph
from matrix_utils import search_field
from config import FieldType

class Dijkstra:

    def __init__(self, start_graph):
        self.graph = copy.deepcopy(start_graph)

    def do_step(self):
        if self.last_node:
            self.last_node.FieldType = self.last_field_type
        current_node = self.graph.min_distance_unvisited()

        if current_node.field_type == FieldType.end:
            self.mark_path(current_node.predecessor)
            return self.graph, True

        self.last_field_type = current_node.field_type
        current_node.field_type = FieldType.current
        current_node.visited = True

        neighbours = current_node.neighbours
        for i in neighbours:
            distance = current_node.distance + 1
            if distance < i.distance and i.fieldType != FieldType.obstacle:
                i.distance = distance
                i.predecessor = current_node

        self.last_node = current_node
        return self.graph, False


