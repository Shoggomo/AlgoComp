from Tkinter import *
import config


class GUI(object):

    def __init__(self, algorithms):
        self._root = Tk()
        self._top = Frame(self._root)
        self._bottom = Frame(self._root)

        self._visualizations = {algo_id: Visualization(self._top, visual_name) for (algo_id, visual_name) in algorithms}
        self._step_button = Button(self._bottom, text='Step')
        self._play_button = Button(self._bottom, command=self.toggle_play, text='Toggle Play')

        for id, visual in self._visualizations.iteritems():
            visual.grid(row=1, column=id, padx=20)
        self._step_button.grid(row=2, column=0)
        self._play_button.grid(row=2, column=1)
        self._top.pack(side=TOP)
        self._bottom.pack(side=BOTTOM)

    def set_step_func(self, step_func):
        self._step_button['command'] = step_func

    def toggle_play(self):
        if '_playing' not in vars(self):
            self._playing = False
        self._playing = not self._playing
        self.play()

    def play(self):
        if self._playing:
            self._step_button.invoke()
            self._root.after(config.SPEED, self.play)

    def recolor_grid(self, algo_id, color_matrix, finished):
        self._visualizations[algo_id].recolor_grid(color_matrix, finished)

    def init_color_grid(self, algo_id, color_matrix):
        self._visualizations[algo_id].init_color_grid(color_matrix)

    def mainloop(self):
        self._root.mainloop()


class Visualization(Frame):

    def __init__(self, parent, name):
        Frame.__init__(self, parent)
        self._name = name
        self._grid = Grid(self)
        self._label = Label(self, text="%s, Steps: 0" % name)
        self._grid.grid(row=0, column=0)
        self._label.grid(row=1, column=0)
        self._step_count = 0
        self._finished = False

    def init_color_grid(self, color_matrix):
        self._grid.recolor(color_matrix)

    def recolor_grid(self, color_matrix, finish):
        if not self._finished:
            self._finished = finish
            self._step_count += 1
            self.update_label()
            self._grid.recolor(color_matrix)

    def update_label(self):
        self._label['text'] = "%s, Steps: %i" % (self._name, self._step_count)


class Grid(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self._grid_size = config.VISUALBOARD_SIZE
        self._cell_count = config.CELL_COUNT
        self._cell_size = (self._grid_size[0] / self._cell_count[0], self._grid_size[1] / self._cell_count[1])
        self._canvas = Canvas(self, width=self._grid_size[0], height=self._grid_size[1])
        self._canvas.grid(row=0, column=0)
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

