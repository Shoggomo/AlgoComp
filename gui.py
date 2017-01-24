from Tkinter import *
import config


class Visual(object):

    def __init__(self, parent):
        self._board = Visualboard(parent)
        self._text = Label(parent, text="Test Text")

    def recolor(self, color_matrix):
        self._board.recolor(color_matrix)

    def pack(self):
        self._board.pack()
        self._text.pack()


class Visualboard(object):

    def __init__(self, parent):
        self._board_size = config.VISUALBOARD_SIZE
        self._cell_count = config.CELL_COUNT
        self._cell_size = (self._board_size[0] / self._cell_count[0], self._board_size[1] / self._cell_count[1])
        self._canvas = Canvas(parent, width=self._board_size[0], height=self._board_size[1])
        self._cell_id_matrix = self.draw_cells()

    def draw_cells(self):
        cell_id_matrix = []
        for x in range(0, self._board_size[0], self._cell_size[0]):
            cell_id_matrix.append([])
            for y in range(0, self._board_size[1], self._cell_size[1]):
                cell_id = self._canvas.create_rectangle(x, y, x + self._cell_size[0], y + self._cell_size[1], fill="white")
                cell_id_matrix[len(cell_id_matrix)-1].append(cell_id)
        return cell_id_matrix

    def recolor(self, color_matrix):
        for x in range(len(self._cell_id_matrix)):
            for y in range(len(self._cell_id_matrix[x])):
                self._canvas.itemconfigure(self._cell_id_matrix[x][y], fill=color_matrix[x][y])

    def pack(self):
        self._canvas.pack()


class GUI(object):

    def __init__(self):
        self._root = Tk()
        self._frame = Frame(self._root)
        self._visualboard = Visualboard(self._frame)
        self._visualboard.pack()
        self._frame.pack()

    def recolor_visualboard(self, color_matrix):
        self._visualboard.recolor(color_matrix)

    def mainloop(self):
        self._root.mainloop()

