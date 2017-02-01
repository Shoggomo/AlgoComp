from gui import GUI
from config import FieldType
import matrix_utils as mu
from Dijkstra import Dijkstra
from Node import *

def step():
    pass

def play():
    pass


g = Graph()
g.set_start_node(1, 1)
g.set_end_node(6, 6)
g.delete_node((3, 1))
g.delete_node((1, 3))
g.delete_node((2, 2))
c_matrix = mu.graph_to_colormatrix(g)

gui = GUI()
gui.recolor_visualboard(c_matrix)

d = Dijkstra(g)
for _ in range(110):
    d.do_step()
c_matrix = mu.graph_to_colormatrix(d.do_step()[0])
gui.recolor_visualboard(c_matrix)

gui.mainloop()