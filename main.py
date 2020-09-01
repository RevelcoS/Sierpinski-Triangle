from lib import Triangle
import tkinter as tk

width = 1200
height = 347 * 3
gen = 8

root = tk.Tk()
root.title("Sierpinski Triangle")
root.wm_attributes("-topmost", True)
canvas = tk.Canvas(root, width=width, height=height, bg="black")
canvas.pack(fill=tk.BOTH, expand=True)
canvas.focus_set()


options = {
    "canvas":canvas,
    "width":width,
    "height":height
}

trig = Triangle(**options)
for i in range(gen):
    trig.next_gen()


root.mainloop()