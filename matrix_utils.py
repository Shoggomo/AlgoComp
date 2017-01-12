from config import FieldType
import config
import random


def empty_matrix():
    l = config.CELL_COUNT[0]
    w = config.CELL_COUNT[1]
    return [x[:] for x in [[FieldType.unvisited] * l] * w]


def get_color_by_fieldtype(fieldtype):
    colors = {
        FieldType.unvisited : "white",
        FieldType.visited : "grey",
        FieldType.start: "blue",
        FieldType.end: "red",
        FieldType.current: "orange",
        FieldType.obstacle: "black",
        FieldType.path: "pink",
    }
    return colors[fieldtype]


def color_matrix(fieldtype_matrix):
    color_matrix = []
    for l in fieldtype_matrix:
        color_matrix.append(map(lambda x: get_color_by_fieldtype(x), l))
    return color_matrix


def random_assign_field(matrix, fieldtype):
    i = random.randint(0, len(matrix)-1)
    j = random.randint(0, len(matrix[i])-1)
    matrix[i][j] = fieldtype


def random_matrix(obstacle_count):
    matrix = empty_matrix()
    for _ in range(obstacle_count):
        random_assign_field(matrix, FieldType.obstacle)
    random_assign_field(matrix, FieldType.start)
    random_assign_field(matrix, FieldType.end)
    return matrix


def search_field(matrix, fieldtype):
    for i, e in enumerate(matrix):
        for j, g in enumerate(e):
            if g is fieldtype:
                return i, j
    return -1, -1
