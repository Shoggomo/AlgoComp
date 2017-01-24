from gui import GUI
from config import FieldType
import matrix_utils as mu
from Node import *

def step():
    pass

def play():
    pass


g = Graph()
g[(1, 3)].distance = 300
g.set_start_node(1, 1)
print [i.distance for i in g[(1, 2)].neighbours]
print g[(1, 4)]

if __name__:
    pass
    #matrix = mu.random_matrix(5)
    #print mu.search_field(matrix, FieldType.start)
    #c_matrix = mu.color_matrix(matrix)

    #gui = GUI()
    #gui.recolor_visualboard(c_matrix)
    #gui.mainloop()
