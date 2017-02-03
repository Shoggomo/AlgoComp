import copy
from graph import Node
from graph import Graph
from config import FieldType

class Dijkstra:

    def __init__(self, start_graph):
        self.graph = copy.deepcopy(start_graph)
        self.last_node = None

    def do_step(self):
        if self.last_node:
            self.last_node.field_type = self.last_field_type
        current_node = self.graph.min_distance_unvisited(None)

        if not current_node:
            return self.graph, True

        if current_node.field_type == FieldType.end:
            self.graph.mark_path(current_node.predecessor)
            return self.graph, True

        self.last_field_type = current_node.field_type
        current_node.field_type = FieldType.current
        current_node.visited = True

        neighbours = current_node.neighbours
        for i in neighbours:
            distance = current_node.distance + 1
            if distance < i.distance and i.field_type != FieldType.obstacle:
                i.distance = distance
                i.predecessor = current_node

        self.last_node = current_node
        return self.graph, False


