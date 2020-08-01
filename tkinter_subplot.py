# Author: Nelson Luu
# Created: 1/08/2020
# Last Modified: 1/08/2020
# Description: Setup GUI for user to interact and decide which graphs to plot (aim to work with data_read.py)
# Last Update:

import tkinter as tk

root = tk.Tk()
# thelabel = tk.Label(root, text="hello")
# thelabel.pack()

root.wm_title("Title")


def plot_graph():
    from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
    from matplotlib.figure import Figure
    # source= https://matplotlib.org/3.1.0/gallery/user_interfaces/embedding_in_tk_sgskip.html

    fig = Figure(figsize=(5, 4), dpi=100)
    x = [0, 1, 2, 3, 4]
    y = [10, 20 , 50, 100, 250]
    fig.add_subplot(111).plot(x, y)

    canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

def _quit():
    root.quit()
    root.destroy()

# buttons
quit_button = tk.Button(master=root, text="Quit", command=_quit)
quit_button.pack(side=tk.BOTTOM)

plot_button = tk.Button(master=root, text="Plot", command=plot_graph)
plot_button.pack(side=tk.TOP)

root.mainloop()