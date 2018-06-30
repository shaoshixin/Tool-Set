import tkinter as tk


class OpenFile(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self,master)
        self.root = master
        # self.openfile_frm1 = Frame(self.root)
        tk.Label(self, text='打开文件！').pack()
