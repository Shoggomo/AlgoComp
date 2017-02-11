import copy
from config import FieldType


class aStar:
    def __init__(self, start_graph):
         self.graph = copy.deepcopy(start_graph)
         self.last_node = None

    def do_step(self):

        def heuristic(goal):
            def program(a):
                return abs(goal.x - a.x) + abs(goal.y - a.y)
            return program

        if self.last_node:
            self.last_node.field_type = self.last_field_type
        current_node = self.graph.min_distance_unvisited(heuristic(self.graph.get_end_node()))
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



