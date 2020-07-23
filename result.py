from tkinter import *
from tkinter.scrolledtext import ScrolledText
root = Tk()
root.geometry("100x300")
v = Scrollbar(root, orient=VERTICAL)
v.pack(side=RIGHT, fill=Y)
output_canvas = Canvas(root, width=50, height=300, scrollregion=[0, 0, 40, 5000])
output_canvas.configure(yscrollcommand=v.set)

v.config(command=output_canvas.yview)

scroll = Canvas(output_canvas, height=4820, width=50)


scroll.pack(side=LEFT)
scrolled = output_canvas.create_window(0, 0, window=scroll, anchor=N)

for i in range(200):
    example = Label(scroll, text=str(i), font=7)
    example.pack()
output_canvas.pack(side=LEFT)
output_canvas.configure(scrollregion=output_canvas.bbox("all"))

root.mainloop()
"""
parent = Tk()
canvas = Canvas(parent, width=150, height=150)
canvas.create_oval(10, 10, 20, 20, fill="red")
canvas.create_oval(200, 200, 220, 220, fill="blue")
canvas.grid(row=0, column=0)

scroll_x = Scrollbar(parent, orient="horizontal", command=canvas.xview)
scroll_x.grid(row=1, column=0, sticky="ew")

scroll_y = Scrollbar(parent, orient="vertical", command=canvas.yview)
scroll_y.grid(row=0, column=1, sticky="ns")

canvas.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
canvas.configure(scrollregion=canvas.bbox("all"))
parent.mainloop()
"""