from tkinter import *
tk = Tk()
canvas = Canvas(tk, width = 400, height = 400)
canvas.pack()

canvas.create_polygon(10, 10, 100, 10, 10, 110, 100, 110, fill = "", outline = "red")
