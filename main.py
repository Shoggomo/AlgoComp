from gui import GUI
from config import FieldType
import matrix_utils as mu

def step():
    pass

def play():
    pass

if __name__:
    matrix = mu.random_matrix(5)
    print mu.search_field(matrix, FieldType.start)
    c_matrix = mu.color_matrix(matrix)

    gui = GUI()
    gui.recolor_visualboard(c_matrix)
    gui.mainloop()
