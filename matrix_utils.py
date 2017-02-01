from config import FieldType


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
