from gui import GUI
from Dijkstra import Dijkstra
from graph import *
import config
from aStar import aStar


def step(gui, *algorithms):
    def do_step():
        for i, algorithm in enumerate(algorithms):
            graph, finished = algorithm.do_step()
            c_matrix = graph_to_colormatrix(graph)
            gui.recolor_grid(i, c_matrix, finished)
    return do_step

if __name__ == "__main__":
    graph = create_random_graph(config.CELL_COUNT[0], config.CELL_COUNT[1], config.OBSTACLE_COUNT)
    dijkstra = Dijkstra(graph)
    d2 = aStar(graph)    #REPLACE WITH OTHER ALGORITHMS
    algo_names = [[0, "Dijkstra"], [1, "A*"]]

    gui = GUI(algo_names)
    step_func = step(gui, dijkstra, d2)
    gui.set_step_func(step_func)

    c_matrix = graph_to_colormatrix(graph)
    for i, _ in algo_names:
        gui.init_color_grid(i, c_matrix)

    gui.mainloop()
