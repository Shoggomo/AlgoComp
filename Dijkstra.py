import copy
from Node import Node
from Node import Graph
from matrix_utils import search_field
from config import FieldType

class Dijkstra:

    def __init__(self, start_graph):
        self.graph = copy.deepcopy(start_graph)

    def mark_path(self, node):
        if node.field_type != FieldType.start:
            node.field_type = FieldType.path
            self.mark_path(node.predecessor)

    def do_step(self):
        if self.last_node:
            self.last_node.FieldType = self.last_field_type
        current_node = self.graph.getNextNode()

        if current_node.field_type == FieldType.end:
            self.mark_path(current_node.predecessor)
            return self.graph, True

        self.last_field_type = current_node.field_type
        current_node.field_type = FieldType.current
        current_node.visited = True

        neighbours = current_node.neighbours
        for i in neighbours:
            distance = current_node.distance + 1
            if distance < i.distance:
                i.distance = distance
                i.predecessor = current_node

        self.last_node = current_node
        return self.graph, False


