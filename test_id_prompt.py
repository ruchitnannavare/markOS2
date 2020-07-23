the_other_output_canvas = Canvas(output_canvas, width=948)
the_other_output_canvas.pack(side=LEFT)

scroll_lord = output_canvas.create_window(0, 0, window=the_other_output_canvas, anchor=NW)
output_canvas.configure(scrollregion=output_canvas.bbox("all"))