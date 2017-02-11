import config
from Dijkstra import Dijkstra
from aStar import aStar
from graph import *
from gui import GUI


def step(gui, *algorithms):
    def do_step():
        for i, algorithm in enumerate(algorithms):
            graph, finished = algorithm.do_step()
            c_matrix = graph_to_colormatrix(graph)
            gui.recolor_grid(i, c_matrix, finished)
    return do_step


def main():
    graph = create_random_graph(config.CELL_COUNT[0], config.CELL_COUNT[1], config.OBSTACLE_COUNT)
    dijkstra = Dijkstra(graph)
    astar = aStar(graph)
    algo_names = [[0, "Dijkstra"], [1, "A*"]]

    gui = GUI(algo_names)
    step_func = step(gui, dijkstra, astar)
    gui.set_step_func(step_func)

    c_matrix = graph_to_colormatrix(graph)
    for i, _ in algo_names:
        gui.init_color_grid(i, c_matrix)

    gui.mainloop()


if __name__ == "__main__":
    main()
