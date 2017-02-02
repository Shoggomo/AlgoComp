from Tkinter import *
import config


class GUI(object):

    def __init__(self):
        self._root = Tk()
        self._frame = Frame(self._root)
        self._dijkstra_visual = Visualization(self._frame, "Dijkstra")
        self._step_button = Button(self._frame, text='Step')
        self._play_button = Button(self._frame, command=self.play, text='Play')
        self._dijkstra_visual.pack()
        self._step_button.pack()
        self._play_button.pack()
        self._frame.pack()

    def set_step_func(self, step_func):
        self._step_button['command'] = step_func

    def play(self):
        self._step_button.invoke()
        self._root.after(config.SPEED, self.play)

    def recolor_grid(self, color_matrix, finished):
        self._dijkstra_visual.recolor_grid(color_matrix, finished)

    def mainloop(self):
        self._root.mainloop()


class Visualization(object):

    def __init__(self, parent, name):
        self._grid = Grid(parent)
        self._name = name
        self._label = Label(parent, text="%s, Steps: 0" % name)
        self._step_count = 0
        self._finished = False

    def recolor_grid(self, color_matrix, finish):
        if not self._finished:
            self._finished = finish
            self._step_count += 1
            self.update_label()
            self._grid.recolor(color_matrix)

    def update_label(self):
        self._label['text'] = "%s, Steps: %i" % (self._name, self._step_count)

    def pack(self):
        self._grid.pack()
        self._label.pack()


class Grid(object):

    def __init__(self, parent):
        self._grid_size = config.VISUALBOARD_SIZE
        self._cell_count = config.CELL_COUNT
        self._cell_size = (self._grid_size[0] / self._cell_count[0], self._grid_size[1] / self._cell_count[1])
        self._canvas = Canvas(parent, width=self._grid_size[0], height=self._grid_size[1])
        self._cell_id_matrix = self.draw_cells()

    def draw_cells(self):
        cell_id_matrix = []
        for x in range(0, self._grid_size[0], self._cell_size[0]):
            cell_id_matrix.append([])
            for y in range(0, self._grid_size[1], self._cell_size[1]):
                cell_id = self._canvas.create_rectangle(x, y, x + self._cell_size[0], y + self._cell_size[1], fill="white")
                cell_id_matrix[len(cell_id_matrix)-1].append(cell_id)
        return cell_id_matrix

    def recolor(self, color_matrix):
        for x in range(len(self._cell_id_matrix)):
            for y in range(len(self._cell_id_matrix[x])):
                self._canvas.itemconfigure(self._cell_id_matrix[x][y], fill=color_matrix[x][y])

    def pack(self):
        self._canvas.pack()

