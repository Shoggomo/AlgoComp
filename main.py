from gui import GUI
from config import FieldType
import matrix_utils as mu
from Node import *

def step():
    pass

def play():
    pass


g = Graph()
g.set_start_node(1, 1)
for n in g.nodes:
    print "(%2i, %2i, %i)" % (n.x, n.y, n.distance)

n = g.min_distance_unvisited(lambda x: x)
print "%i, %i, %i" % (n.x, n.y, n.distance)

if __name__:
    pass
    #matrix = mu.random_matrix(5)
    #print mu.search_field(matrix, FieldType.start)
    #c_matrix = mu.color_matrix(matrix)

    #gui = GUI()
    #gui.recolor_visualboard(c_matrix)
    #gui.mainloop()
