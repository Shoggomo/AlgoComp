from gui import GUI
from Dijkstra import Dijkstra
from graph import *
import config


def step(gui, *algorithms):
    def do_step():
        for algorithm in algorithms:
            graph, finished = algorithm.do_step()
            c_matrix = graph_to_colormatrix(graph)
            gui.recolor_grid(c_matrix, finished)
    return do_step


def create_graph():
    g = Graph(config.CELL_COUNT[0], config.CELL_COUNT[1])
    g.set_start_node(1, 1)
    g.set_end_node(6, 6)
    obstacles = ((3, 1), (1, 3), (2, 2), (3, 0), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8))
    map(lambda o: g.delete_node(o), obstacles)
    return g


if __name__ == "__main__":
    graph = create_graph()
    dijkstra = Dijkstra(graph)

    gui = GUI()
    step_func = step(gui, dijkstra)
    gui.set_step_func(step_func)
    c_matrix = graph_to_colormatrix(graph)
    gui.recolor_grid(c_matrix, False)

    gui.mainloop()
