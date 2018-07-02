import tkinter as tk


class TestData(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.root = master
        # self.openfile_frm1 = Frame(self.root)
        tk.Label(self, text='测试文件生成！').pack()
