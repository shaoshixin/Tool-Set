import tkinter as tk


class XML(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.root = master
        tk.Label(self, text='xml！').pack()
