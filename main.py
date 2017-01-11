from Tkinter import *



def draw_chessboard(canvas, width, height, cell_width, cell_height):
    matrix = []
    for x in range(0, width, cell_width):
        matrix.append([])
        for y in range(0, height, cell_height):
            id = canvas.create_rectangle(x, y, x+cwidth, y+cheight, fill="white")
            matrix[len(matrix)-1].append(id)
    return matrix


cwidth = 50
cheight = 50

width = 500
height = 500

root = Tk()
frame = Frame(root)
frame.pack()
canvas = Canvas(frame, width=width, height=height)
canvas.pack()

ids = draw_chessboard(canvas, width, height, cwidth, cheight)
print ids

#canvas.itemconfigure(1, fill="red")

root.mainloop()