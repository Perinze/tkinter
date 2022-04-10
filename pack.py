import tkinter as tk

window = tk.Tk()

frm1 = tk.Frame(master=window, width=100, height=100, bg="red")
frm1.pack()

frm2 = tk.Frame(master=window, width=50, height=50, bg="yellow")
frm2.pack()

frm3 = tk.Frame(master=window, width=25, height=25, bg="blue")
frm3.pack()

window.mainloop()